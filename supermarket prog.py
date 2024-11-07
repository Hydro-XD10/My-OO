class Super_market:
    def __init__(self,frozen_foods,fresh_fruit,veggi,tinned_goods,pharmacy):
        self.frozen_foods=[]
        self.fresh_fruit=[]
        self.veggi=[]
        self.tinned_goods=[]
        self.pharmacy=[]
        
    def add_product(self, section_name, the_product):
        if section_name == "frozen_foods":
            self.frozen_foods.append(the_product)
        elif section_name == "fresh_fruit":
            self.fresh_fruit.append(the_product)
        elif section_name == "veggi":
            self.veggi.append(the_product)
        elif section_name == "tinned_goods":
            self.tinned_goods.append(the_product)
        elif section_name== "pharmacy":
            self.pharmacy.append(the_product)
        return
                   
        #return section.append(the_product)
    def show_products(self):
        print("Frozen Foods stock:", superm.frozen_foods)
        print("fresh_fruit stock:", superm.fresh_fruit)
        print("veggi stock:", superm.veggi)
        print("tinned_goods stock:", superm.tinned_goods)
        print("pharmacy stock:", superm.pharmacy)
    
    
        
superm= Super_market([],[],[],[],[])
superm.add_product("frozen_foods", "Frozen mango peaces")


superm.show_products()

#print("Frozen Foods:", superm.frozen_foods)
    
    