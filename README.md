# Ecommerce con Django

`python manage.py runserver`

Se creó una app ecommerce

*{localhost:puerto}/ecommerce/*

que renderiza el template 'home'. A pesar del nombre, que es la idea final del proyecto, es en realidad una app de gestión para un negocio.

En el navbar se incluyeron las referencias a 5 secciones navegables:
- El inicio (home)
- Productos, todos (*{localhost:puerto}/ecommerce/products/*) u ordenados por precio (*{localhost:puerto}/ecommerce/ordered_products/*)
- Empleados (*{localhost:puerto}/ecommerce/employees/*)
- Proveedores (*{localhost:puerto}/ecommerce/suppliers/*)
- Ingresar (*{localhost:puerto}/ecommerce/login/*)
La sección de **login** también permite el registro de nuevos usuarios (*{localhost:puerto}/ecommerce/register/*). Algunas secciones solo son accesibles para usuarios logueados y/o para el superusuario (*user*: **milog**, *password*: **log12345**), particularmente para modificar información. Las secciones de **Productos**, **Empleados** y **Proveedores**, proveen entonces formularios según los respectivos modelos para agregar un nuevo elemento a la base de datos, actualizar los existentes, o eliminarlos. La sección de **Busqueda**, permite obtener un producto, un empleado o un proveedor por sus nombres.
Tanto al crear, como al modificar productos, es posible agregar una imagen de los mismos. Por último, para los usuarios logueados es posible acceder a "Actualizar Perfil", para modificar sus datos (nombre y apellido, email, y contraseña).
Para la herencia html se utiliza `include`, con definición de algunos componentes (header, navbar, footer).