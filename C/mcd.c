#include <stdio.h>


int mcd(int a, int b);
int mcdr(int a, int b);


int main(int argc, char* argv[])
{
	
	int a,b;
	
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	/*
	printf("Ingrese a\n");
	scanf("%d",&a);
	
	printf("Ingrese b\n");
	scanf("%d",&b);*/
	
	printf("mcd(a,b) = mcd(%d,%d) = %d",a,b,mcdr(a,b));
}
//Calculo del mcd de a y b usando el algoritmo de Euclides.
int mcd(int a, int b)
{
	int aux;
	
	if(a == 0 || b == 0) return -1; //Error.
	
	//Si  a < b invierto los valores para poder aplicar el algortimo.
	if(a < b)
	{
		aux = a;
		a = b;
		b = aux;
		}	
		
	while(b!= 0 && a%b != 0 )
	{
		aux  = b;
		b = a%b;
		a = aux;
								
	};	 
	
	return b;
}

int mcdr(int a,int b)
{

	if(a%b != 0)
		return mcdr(b,a%b);
	
	return b;				
}



