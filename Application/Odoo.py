import xmlrpc.client
from tkinter import Tk

class ErpOdoo:
    def __init__(self):
        self.url = 'http://172.31.11.129:8069'
        self.db = 'MyFactory'
        self.models = None  # Initialisation à None, sera configuré lors de la connexion
        self.uid = None  # Initialisation à None, sera configuré lors de la connexion

    def connexion(self, username, password):
        try:
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
            self.uid = common.authenticate(self.db, username, str(password), {})  # Convertissez le mot de passe en chaîne
            self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
            return self.models, self.uid
        except Exception as e:
            print("Erreur de connexion à Odoo:", e)
            return None, None

    def get_department_id(self, uid, password):
    
        # Remplacez 'res.users' par le modèle Odoo correspondant à votre utilisateur
            user_data = self.models.execute_kw(self.db, uid, password, 'res.users', 'read', [[uid]], {'fields': ['department_id']})

            if user_data:
                department_id = user_data[0]['department_id'][0]  # Récupérer le premier élément s'il y en a plusieurs
                return department_id

    def recuperer_of_en_attente(self, uid, password):
        # Récupérer les OF en attente à l'état "confirmed" et "to close" depuis Odoo
        of_records = self.models.execute_kw(self.db,uid, password,
                                                 'mrp.production', 'search_read',
                                                 [[('state', 'in', ['confirmed'])]],
                                                 {'fields': ['name', 'product_id', 'product_qty', 'qty_producing']})

        return of_records

    def recuperer_of_en_cours(self, uid, password):
        # Récupérer les OF en cours avec les mouvements de stock depuis Odoo
        of_records = self.models.execute_kw(self.db, uid, password,
                                                    'mrp.production', 'search_read',
                                                    [[('state', 'in', ['progress', 'to_close'])]],
                                                    {'fields': ['name', 'product_id', 'product_qty', 'qty_producing','move_raw_ids']})
        return of_records

    def passer_en_attente(self, selected_of, uid, password):
        self.models.execute_kw(self.db, uid, password,
                                    'mrp.production', 'write',
                                    [[selected_of['id']], {'state': 'confirmed'}])

    def passer_en_cours(self,selected_of, uid, password):
        # Vérifier s'il n'y a pas d'OF en cours
        self.models.execute_kw(self.db, uid, password,
                                    'mrp.production', 'write',
                                    [[selected_of['id']], {'state': 'progress'}])

    def passer_en_fait(self,selected_of,uid,password):
        self.models.execute_kw(self.db, uid, password, 'mrp.production', 'button_mark_done', [[selected_of['id']]])

    def modifier_quantite_en_cours(self, selected_of,nouvelle_quantite_produite,uid,password):
        #modifier la quantité de l'of en cours
        self.models.execute_kw(self.db, uid, password,
                                            'mrp.production', 'write',
                                            [[selected_of['id']], {'qty_producing': nouvelle_quantite_produite}])                                                            
        move_ids = selected_of.get('move_raw_ids', [])
        for move_id in move_ids:
            # Mettre à jour la quantité consommée dans chaque mouvement de stock
            self.models.execute_kw(self.db, uid, password,
                                    'stock.move', 'write',
                                    [[move_id], {'quantity_done': nouvelle_quantite_produite}])
    def obtenir_artcles_photo(self, uid, password):
        article_model = 'product.template'
        article_fields = ['id', 'name', 'image_1920', 'qty_available']
        article_ids = self.models.execute_kw(self.db, uid, password,
                                         article_model, 'search', [[]], {'limit': 7})
        articles = self.models.execute_kw(self.db, uid, password,
                                       article_model, 'read', [article_ids], {'fields': article_fields})
        return articles

    def modifier_stock_article(self,article_id,nouvelle_quantite,uid,password):
        article = self.models.execute_kw(self.db, uid, password, 'product.product', 'search_read', [[('id', '=', article_id)]], {'limit': 1})

        if not article:
            print(f"Aucun article trouvé avec l'ID {article_id}. Vérifiez l'ID de l'article.")
        else:
            # Création d'une nouvelle entrée pour changer la quantité
            stock_change_product_qty_id = self.models.execute_kw(self.db, uid,password, 'stock.change.product.qty', 'create', [{
                'product_id': article_id,
                'product_tmpl_id': article[0]['product_tmpl_id'][0],
                'new_quantity': nouvelle_quantite,}])

            # Exécution de la méthode change_product_qty pour appliquer le changement
            self.models.execute_kw(self.db, uid,password, 'stock.change.product.qty', 'change_product_qty', [stock_change_product_qty_id])

            #print(f"La quantité en stock de l'article {article_id} a été modifiée avec succès.")

    def obtenir_reception_en_attente(self, uid, password):
        # Récupération des identifiants des réceptions entrantes en attente avec les statuts 'assigned' et 'confirmed'
        receptions_ids =self. models.execute_kw(self.db, uid, password,
        'stock.picking', 'search',
        [[('state', 'in', ['assigned', 'confirmed']), ('picking_type_code', '=', 'incoming')]])

        # Récupération des données des réceptions
        receptions_data = self.models.execute_kw(self.db, uid, password,
        'stock.picking', 'read',
        [receptions_ids], {'fields': ['id', 'name', 'date', 'partner_id']})
        return receptions_data

    def obtenir_livraison_en_attente(self, uid, password):
        livraison_ids =self. models.execute_kw(self.db, uid, password,
        'stock.picking', 'search',
        [[('state', 'in', ['assigned', 'confirmed']), ('picking_type_code', '=', 'outgoing')]])

        # Récupération des données des livraisons
        livraison_data = self.models.execute_kw(self.db, uid, password,
        'stock.picking', 'read',
        [livraison_ids], {'fields': ['id', 'name', 'date', 'partner_id']})
        return livraison_data
    
    def passer_a_fait_expedition(self, picking_id, uid, password):
         self.models.execute_kw(self.db, uid, password,'stock.picking', 'button_validate',[[picking_id]])
#####################################################################################################################################
class User:
    def __init__(self, username, password, models,uid) -> None:
        self.username= username
        self.password = password
        self.models = models
        self.uid = uid 
        self.department_id = None

