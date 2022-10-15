#Comando para mostrar a pasta/diretório em que se está.
current_directory=$(pwd)
echo 'Your current directory is' $current_directory

#Comando para imprimir a data atual na tela.
current_date=$(date)
echo "Right now, it's" $current_date

#Comando para gerar uma lista com detalhes do conteúdo da pasta HOME, redirecionando a saída para outro arquivo.
ls -lF /home > lista_HOME.txt
