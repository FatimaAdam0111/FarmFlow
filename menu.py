
from PyQt6 import QtWidgets, uic
from plot import PlotWindow
from crop import CropWindow
from livestock import LivestockWindow
from workstation import WorkstationWindow
from products import ProductsWindow
from cropcycle import CropCycleWindow
from production import ProductionWindow
from inventory import InventoryWindow
from recipe import RecipeWindow
from ingredients import IngredientsWindow


class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Menu.ui", self)

        self.PLOTBUTTON.clicked.connect(self.open_plot)
        self.CROPBUTTON.clicked.connect(self.open_crop)
        self.LIVESTOCKBUTTON.clicked.connect(self.open_livestock)
        self.WORKSTATIONBUTTON.clicked.connect(self.open_workstation)
        self.PRODUCTSBUTTON.clicked.connect(self.open_products)
        self.CYCLEBUTTON.clicked.connect(self.open_cycle)
        self.PRODUCTIONBUTTON.clicked.connect(self.open_production)
        self.INVENTORYBUTTON.clicked.connect(self.open_inventory)
        self.RECIPEBUTTON.clicked.connect(self.open_recipe)
        self.INGREDIENTSBUTTON.clicked.connect(self.open_ingredients)

    def open_plot(self):
        self.next_window = PlotWindow()
        self.next_window.show()
        self.close()

    def open_crop(self):
        self.next_window = CropWindow()
        self.next_window.show()
        self.close()

    def open_livestock(self):
        self.next_window = LivestockWindow()
        self.next_window.show()
        self.close()

    def open_workstation(self):
        self.next_window = WorkstationWindow()
        self.next_window.show()
        self.close()

    def open_products(self):
        self.next_window = ProductsWindow()
        self.next_window.show()
        self.close()

    def open_cycle(self):
        self.next_window = CropCycleWindow()
        self.next_window.show()
        self.close()

    def open_production(self):
        self.next_window = ProductionWindow()
        self.next_window.show()
        self.close()

    def open_inventory(self):
        self.next_window = InventoryWindow()
        self.next_window.show()
        self.close()

    def open_recipe(self):
        self.next_window = RecipeWindow()
        self.next_window.show()
        self.close()

    def open_ingredients(self):
        self.next_window = IngredientsWindow()
        self.next_window.show()
        self.close()
