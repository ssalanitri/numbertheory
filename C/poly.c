#include <stdio.h>
#include <math.h>

#define N 20
//Libreria con funciones de analisis matematico.
void poly(int n,int g,double *c,double *f);


int main(int argc, char**argv)
{
	int i;
	int n = N;
	int grado;
	
	if(argc == 2)
	{
	    grado = atoi(argv[1]);
	    printf("Polinimio de grado: %d",grado);
	}
	else
	{
	    printf("Grado: ");
	    scanf("%d",&grado);
	}
	
	double coef[grado+1];
	double funcion[2*n+1];  //Quiero tomar desde -n a n.
	
	for(i=grado;i>=0;i--)
	{
		printf("\nIngrese coeficiente de x^%d:",i);
		scanf("%lf",&coef[i]);
	}	
        for(i=grado; i >= 0; i--)
            printf("Coef x^%d: %f, ",i,coef[i]);
	
		puts("\n");
		poly(n,grado,coef,funcion);
		
	return 0;
}

void poly(int n,int g,double *c,double *f)
{
//	int n = 20;
	float x;
	int i=0;
			
	//Cargo coeficientes
	//Ej: x^3-x-1
	/*c[g] = 1;
	c[g-1] = 0;
	c[g-2] = -1;
	c[g-3] = -1;
	*/
	
	 //Genero los valores de la funciona entre -n y n con pasos de 0.01
	
	i = 0;
	int xn;
		
	printf("  xn		f(xn)\n");

	for( xn = -n; xn <= n; xn++ )
	{
		for(i=0 ; i<=g; i++)
		{
			f[xn+n]+= c[g-i]*pow(xn,g-i);
		}
		
	}
	

	for(xn = 0; xn <= 2*n; xn++ )
	{
		printf("  %d  		%f\n",xn-n,f[xn]);
	}	
	
	for(xn = 0; xn <= 2*n; xn++)
		printf("%f, ",f[xn]);
		
	printf("\n");

}


