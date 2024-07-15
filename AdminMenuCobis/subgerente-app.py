import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación Subgerente")
        self.setGeometry(100, 100, 800, 600)

        # Widget central y layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Crear el menú principal
        self.create_menu()

        # Crear el widget apilado para las diferentes pantallas
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Crear las pantallas principales
        self.create_cajas_screen()
        self.create_depositos_plazo_fijo_screen()
        self.create_depositos_vista_screen()
        self.create_cartera_screen()
        self.create_clientes_screen()

    def create_menu(self):
        menu_bar = self.menuBar()

        # Menú Cajas
        cajas_menu = menu_bar.addMenu("CAJAS")
        cajas_menu.addAction("Administración de Caja", self.show_cajas)
        cajas_menu.addAction("Consultas", self.show_cajas)
        cajas_menu.addAction("Transacciones de Caja", self.show_cajas)

        # Menú Depósitos a Plazo Fijo
        dpf_menu = menu_bar.addMenu("DEPÓSITOS A PLAZO FIJO")
        dpf_menu.addAction("Búsqueda de Depósitos", self.show_depositos_plazo_fijo)
        dpf_menu.addAction("Simular", self.show_depositos_plazo_fijo)
        dpf_menu.addAction("Apertura", self.show_depositos_plazo_fijo)
        dpf_menu.addAction("Consultas", self.show_depositos_plazo_fijo)

        # Menú Depósitos a la Vista
        dv_menu = menu_bar.addMenu("DEPÓSITOS A LA VISTA")
        dv_menu.addAction("Consultas", self.show_depositos_vista)
        dv_menu.addAction("Operaciones", self.show_depositos_vista)

        # Menú Cartera
        cartera_menu = menu_bar.addMenu("CARTERA")
        cartera_menu.addAction("Consultas", self.show_cartera)

        # Menú Clientes
        clientes_menu = menu_bar.addMenu("CLIENTES")
        clientes_menu.addAction("Operaciones", self.show_clientes)

    def create_cajas_screen(self):
        cajas_widget = QWidget()
        layout = QVBoxLayout(cajas_widget)
        layout.addWidget(QLabel("Pantalla de Cajas"))
        # Aquí puedes añadir más widgets específicos para la sección de Cajas
        self.stacked_widget.addWidget(cajas_widget)

    def create_depositos_plazo_fijo_screen(self):
        dpf_widget = QWidget()
        layout = QVBoxLayout(dpf_widget)
        layout.addWidget(QLabel("Pantalla de Depósitos a Plazo Fijo"))
        # Añadir más widgets para Depósitos a Plazo Fijo
        self.stacked_widget.addWidget(dpf_widget)

    def create_depositos_vista_screen(self):
        dv_widget = QWidget()
        layout = QVBoxLayout(dv_widget)
        layout.addWidget(QLabel("Pantalla de Depósitos a la Vista"))
        # Añadir más widgets para Depósitos a la Vista
        self.stacked_widget.addWidget(dv_widget)

    def create_cartera_screen(self):
        cartera_widget = QWidget()
        layout = QVBoxLayout(cartera_widget)
        layout.addWidget(QLabel("Pantalla de Cartera"))
        # Añadir más widgets para Cartera
        self.stacked_widget.addWidget(cartera_widget)

    def create_clientes_screen(self):
        clientes_widget = QWidget()
        layout = QVBoxLayout(clientes_widget)
        layout.addWidget(QLabel("Pantalla de Clientes"))
        # Añadir más widgets para Clientes
        self.stacked_widget.addWidget(clientes_widget)

    def show_cajas(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_depositos_plazo_fijo(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_depositos_vista(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_cartera(self):
        self.stacked_widget.setCurrentIndex(3)

    def show_clientes(self):
        self.stacked_widget.setCurrentIndex(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
