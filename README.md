# TRABAJO-EV1-POO2
Trabajo #1 de la asignatura Programacin Orientada a Objetos 2. 

Consiste en desarrollar una API Rest con Flask y Python.

Se deben Cumplir los Siguientes Requisitos:

# Requisitos
El trabajo es de carácter individual
Solo debe utilizar Flask y las utilidades de Python
Debe ser entregado via Canvas. La entrega es un link a un repositorio Git con el código de la aplicación
El estado de la aplicación debe persistir en memoria
Debe asistir a la clase del día martes 15 de Abril en que se entregará el trabajo ya que parte de la evaluación consiste en contestar 2 preguntas del docente con respecto a su código
Tiene la posibilidad de realizar una API REST que devuelva JSON, o implementar una interfaz HTML que cumpla las funciones descritas.
De realizar la API REST, el trabajo debe de contener un archivo llamado "peticiones.http" con las peticiones que se pueden realizar a la API con la extension REST Client de Visual Studio Code, según lo visto en clases


Se debe desarrollar los siguientes END POINTS:

# END POINTS

# Listar Recordatorios
Debe poder listar todos los recordatorios previamente creados. Estos recordatorios deben contar con 4 propiedades: “id”, “content”, "createdAt" e “important”. 

Los recordatorios deben ser ordenados de la siguiente manera: Aquellos recordatorios que están marcados como importantes siempre deben ir primero. Luego le siguen los recordatorio que no están marcados como importantes y deben estar ordenados desde la fecha más cercana a la más lejana.

Ruta: /api/reminders
Método: GET
Content-Type: application/json
Salida:
Arreglo de recordatorios
id: string
content: string
createdAt: int
important: boolean
Código de estado con operación correcta: 200
 

# Creación de Recordatorio
Debe poder crear un Recordatorio. Al momento de crear el Recordatorio se le debe proporcionar un id de clase UUID. Este Recordatorio debe ser creado con la propiedad “important” con valor “false”, a menos que se indique lo contrario. La fecha de creación debe de crearse en el servidor, y debe guardarse como un timestamp en milisegundos.

Ruta: /api/reminders
Método: POST
Content-Type: application/json
Entrada:
content: string
important?: boolean (Por defecto false)
Salida:
id: string en formato UUID
content: string
createdAt: int
important: boolean
Código de Estado con operación correcta: 201
Código de Estado con operación incorrecta:
400 si el content o important no fueron enviados correctamente
 

# Actualización de Recordatorio
Debe poder actualizar un Recordatorio de forma parcial. Luego de la actualización, además debe retornar un objeto que represente el nuevo estado del recordatorio actualizado.

Solo debe permitir la actualización de los atributos content e important, no el id o createdAt.

Ruta: /api/reminders/:id
Método: PATCH
Content-Type: application/json
Entrada:
id: string (Por parámetro de ruta)
content?: string
important?: boolean
Salida:
id: string
content: string
createdAt: int
important: boolean
Código de Estado con operación correcta: 200
Código de Estado con operación incorrecta:
400 si al enviar el content o important estos no están en los formatos correctos
404 si el recordatorio a modificar no existe
 

# Borrado de Recordatorio
Debe poder borrar un recordatorio que se encuentre guardado en memoria.

Ruta: /api/reminders/:id
Método: DELETE
Entrada
id: string (Por parámetro de ruta)
Código de Estado con operación correcta: 204
Código de Estado con operación incorrecta:
404 en caso que el recordatorio no exista
 

# Validación de entradas
Al momento de crear o actualizar un recordatorio debe validar lo siguiente:

content:
debe ser un string
no debe estar vacío (Es requerido y no debe ser un string vació o con solo espacios)
Como máximo debe contener 120 caracteres
 important
debe ser un valor booleano

