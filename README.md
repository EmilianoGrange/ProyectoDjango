# Ecommerce con Django

`python manage.py runserver`

Se creo una app ecommerce

*{localhost:puerto}/ecommerce/*

que renderiza el template 'home'

En el navbar se incluyeron las referencias a 6 secciones navegables:
- El inicio (home)
- Productos (Todos) (*{localhost:puerto}/ecommerce/products/*)
- Empleados (*{localhost:puerto}/ecommerce/employees/*)
- Proveedores (*{localhost:puerto}/ecommerce/suppliers/*)
- Busqueda (*{localhost:puerto}/ecommerce/search-product/*)
- Ingresar (no funcional)
Las secciones de **Productos**, **Empleados** y **Proveedores**, proveen formularios segun los respectivos modelos para agregar un nuevo elemento en la base de datos. La sección de **Busqueda**, permite obtener un producto por su nombre.
Para la herencia html se utiliza `include`, con definición de algunos componentes (header, navbar, footer).

## TODO:
- Popular la BD
- Resolver la seccion Ingresar
- Notificaciones cuando se agregan elementos a la BD
- La busqueda (con `get()`) solo permite buscar 1 producto por su nombre. Desarrollarla para los demás modelos, y con diferentes filtros.
- Resolver código comentado (imagenes en los productos, validaciones en los formularios, etc)