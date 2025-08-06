Para utilizar essa automação, você deve se atentar em dois pontos.

1- Arquivo Main.py

Esse sera o arquivo que você devera rodar para a automação rodar

2- Arquivo data.json

Esse é o arquivo que o robô consome para poder fazer o processo. Cada atributo tem seu propósito como veremos agora:

-> Ad_List [LISTA DE STRINGS]: Aqui sera armazenado todos os anúncios que o robô já visitou. Isso evita que ele mande mensagem para o mesmo usuário duas vezes. Caso você queira que ele envie novamente uma mensagem para o anuncio especifico, apenas
delete o link diretamente do arquivo

-> Last_execution [STRING]: Serve para armazenar a ultima vez que o robô executou

-> products [LISTA DE DICIONÁRIOS]: Aqui sera onde ficara o nome do produto (key) e o link da olx para ser encontrado (value). O nome do produto é extremamente importante para evitar que seja enviado mensagem para produtos semelhantes.
ex: Teclado musical é diferente de teclado do computador. 

-> message: Serve para inserir a mensagem que você gostaria que fosse enviada para o usuário final