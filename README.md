# Proyecto Final - Web Inventario
## Participantes
- **Juan Jose Herrera**
- **Juan Pablo Almeida**

## Resumen
Esta web lo que busca es mantener un inventario simple.
Consta por ahora de 3 clases de productos
- Lacteos
- Galletitas
- Bebidas

Cada clase contiene 4 campos

- **Codigo**: El codigo unico de producto
- **Marca**: La marca del fabricante del producto
- **Tipo**: El tipo de producto, alguna característica del producto. (Chocolate, descremada, etc.)
- **Precio**: El precio del producto

# Vistas

## Inicio

![pagina de inicio](ImagenesReadme/StartPage.png)

La pagina de inicio contiene:

* **Inicio**: Una url que lleva a la misma pagina de inicio. Se encuentra disponible en todas las vistas
* **Lacteos**: Url exclusiva a la seccion de lacteos. Por ahora solo lleva a una pagina en blanco con el nombre del producto. Se encuentra disponible en todas las vistas
* **Galletitas**: Url exclusiva a la seccion de galletitas. Por ahora solo lleva a una pagina en blanco con el nombre del producto. Se encuentra disponible en todas las vistas
* **Bebidas**: Url exclusiva a la seccion de bebidas. Por ahora solo lleva a una pagina en blanco con el nombre del producto. Se encuentra disponible en todas las vistas
* **Registro**: Url para el registro de usuarios. Se encuentra disponible solo en la pagina de inicio (Inactivo por el momento.)
* **Agrega producto (formulario manual)**: Url para ir al formulario para agregar productos. Este formulario esta construido de manera manual. Se deja solo a manera de evaluar opciones y para práctica.
* **Agrega producto (Formulario Django)**: Url para ir al formulario para agregar productos. Este formulario esta construido usando las opciones nativas de Django.
* **Buscar producto**: Url para ir al formulario para buscar productos en la base de datos.

## Formularios

### **Formularios para crear**

Los formularios para agregar productos a la base de datos funciona de manera similar. Requieren de 4 campos

![Formulario para crear](ImagenesReadme/FormCreate.png)

- Codigo: Acepta solo numeros.
  - Cuando el codigo empieza con "1", crea productos en la tabla de Lacteos en la BD
  - Cuando el codigo empieza con "2", crea productos en la tabla de Galletitas en la BD
  - Cuando el codigo empieza con "3", crea productos en la tabla de Galletitas en la BD
- Marca: Acepta caracteres alfanumericos
- Tipo: Acepta caracteres alfanumerico
- Precio: Acepta solo numeros

### **Formulario para buscar**

El fomulario para buscar, por ahora necesita solo del codigo del producto. Usa el primer numero del codigo para identificar en cual tabla de producto hacer la busqueda

![Formulario para crearbuscar](ImagenesReadme/FormGet.png)



