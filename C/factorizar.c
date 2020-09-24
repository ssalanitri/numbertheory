#include <stdio.h>
#include <math.h>

#define N 10
#define CICLOS  3

//Factorizacion de un entero.

long factorizar(long n,long *p,long *factores);
long generarPrimos(long n,long *p);

int main(int argc, char* argv[])
{
	long f = 0;
	long n = N;
	long p[n];
	int ciclos;
	long PIn;
	
	if( argc == 2)
		n = atoi(argv[1]);

	//int p = generarPrimo(atoi(argv[1]));
	
	
	for(ciclos = 1; ciclos <= CICLOS; ciclos++)
	{
	    printf("Factorizo para n = %ld\n",n);

		PIn = generarPrimos(n,p);
		
		//Supongo que la lista de factores no será > PI(n)
		long factores[PIn];
		
		long cant_factores = factorizar(n,p,factores);
		
		float PInGauss = n/log(n);
		float errorPorc = 100*(PInGauss - PIn)/PInGauss;
	
		printf("\nFactores primos de n = %ld\n",n);
		
		for(f=0; f < cant_factores; f++)
			printf("%ld, ",factores[f]);

	    printf("PIn     PInGauss     Error\n");
		printf("PI(n) = %ld       PIGauss(n) = %f       Error: %f \n",PIn,PInGauss,errorPorc);
	    
        //Paso al siguiente valor de n.
		n = (long)pow(n,ciclos);  
	}
	
}
//Factorizar: Factoriza el numero n en productos de primos.
//En p esta la lista de todos los primos < n.
// n puede tener más de una vez el mismo factor.

long factorizar(long n,long *p,long *factores)
{
	long f=0;
	long i = 0;
	//Primera versión: a fuerza bruta busco los primos tal que n\p
	
	while(n != 1 )
	{
		
		if( n%p[i] == 0 )
		{	
			factores[f] = p[i];
			n = n/p[i];
			f++;
		}
		else
			i++;
	}
	
	return f;  //Devuelve la cantidad de factores.
}

//Genera los primos < n y devuelve la lista de esos primos y PI(n).

long generarPrimos(long n, long *primos)
{
	//Primera version: Busco en cada llamda el primo para n.
	//Segunda versión: usar vector para cachear los primos para no buscarlos en cada llamda.
	//Uso el metodo de la Criba de Erastostenes.
	
	long criba[n];
	//long primos[n];
	long i,j,p = 0;
	long m = (long)sqrtf(n)+1; //Cant de elemento de la criba a consultar sus múltimplos.
	criba[0] = 0; 
	//Lleno la criba con numeros enteros de 1 a n.
	for(i=1; i <= n; i++ )
	{
		criba[i] = i;
		primos[i] = 0;
	}
	
	//Recorro la criba y reemplazo con ceros los numeros compuestos.
	criba[1] = 0; //el 1 no es primo.

	for(i=2;i<=m;i++)
	{
		for(j=i;j<n;j++)
		{
			if(i == j || criba[j] == 2)continue;
			
			//Busco multiplos
			if(criba[j]%i == 0)
				criba[j] = 0;
				
		}
	}
		
	
	j=0;

	for(i=0; i < n ;i++)
	{
		if(criba[i] != 0)
		{	
			primos[j] = criba[i];
//			printf("%d, ",primos[j]);
			j++;	
		}
	}		
	//En j se carga Pi(n).
	
	return j;
	
}
