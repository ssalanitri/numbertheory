#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int validar(const char **codigo);

void main(void)
{
	const char *codigo[12];
	
	printf("Ingrese codigo\n");
	scanf("%s",&codigo);
	
	if(validar(codigo))
            puts("OK");
        else
            puts("Tarjeta invalida");
		
	return;
}

int validar(const char **codigo)
{
	int val = 0,i=0,j;
	int d,r,cod,sumval;
	
	//Valido que tenga la cantidad de caracteres requerido
	if(strlen(*codigo) != 12) return 0;
	
	//Tomo los valores impares y lo multiplico por 2
		
	while( codigo[i] != '\0')
	{
		if(i%2)
		{
			cod = atoi(codigo[i]) * 2;
			itoa (i,codigo[i],10);
		}
		
		//Los numeros quemultiplicado por 2 dieron mas de 10 
		//sumo sus digitos.
		if(cod >= 10)
		{
			d = cod/10;
			r = cod%10;
		}
		
		i++;
	}
	
	//Sumo lo valores de todos los digitos del codigo.
		
	for(j=0; j < 12; j++)
		sumval += atoi(codigo[j]);
		
	if(!sumval%10)
		val = 1;
	
	
	return val;
}