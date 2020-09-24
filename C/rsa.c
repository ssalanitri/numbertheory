#include <stdio.h>
#include <string.h>

#define true 1
#define false 0


typedef int bool;
int mcd(int a, int b);
char alfabeto[27] = {"abcdefghijklmnopqrstuvwxyz"};
bool es_primo(int n);
int get_pos(char *str,char elemento);
char* validar_mensaje(char* texto_plano);
void desencriptar();
void encriptar();
long  Adicion_Zn(int a,int b,int n);
long Multiplicacion_Zn(int a,int b,int n);
long Inverso_Zn(int a,int n);
long* alg_euc_ext(int n1,int n2); // n1 es a y n2 es b
unsigned long long  Exponenciacion_Zn(unsigned long long  a,unsigned long long  k,unsigned long long  n);



int main(int argc, char *argv[])
{
    int op;
    puts("\n\n         ALGORITMO RSA\n\n");      
           
    puts("    [1] -> ENCRIPTAR\n\n");
    puts("    [2] -> DESENCRIPTAR\n\n");
    puts(" Seleccione una opcion:");
    
    scanf("%d",&op);
        
	if(op==1)
      encriptar();
    if(op==2)
      desencriptar();
     
    return EXIT_SUCCESS;
}

void desencriptar()
{
     puts("\n DESENCRIPTAR :\n\n");
     long int d,n,tam;
     puts(" Ingrese clave privada (d) :");
     scanf("%d",&d);
     
	 cout<<" Ingrese clave n (p*q) :";
     scanf("%d",&n);
     
     cout<<" longitud del mensaje cifrado:";
     scanf("%d",&tam);
      
     long int mensaje_cifrado[tam];
     long int mensaje_int[tam*2];
     char* mensaje="";
      
     puts(" Mensaje cifrado: \n");
     
     for(int i=0;i<tam;i++)
     { 
	 	puts("  ["<<i+1<<"] = ");
		scanf("%s",&mensaje_cifrado[i]);
  	}
      
     // elevamos el mensaje a la potencia d (mod n)
      puts(" mensaje cifrado a la potencia 'd':");
      
      for(int i=0;i<tam;i++)
          mensaje_cifrado[i] = Exponenciacion_Zn(mensaje_cifrado[i],d,n);
          
      for(int i=0;i<tam;i++)
          printf("%c  ",mensaje_cifrado[i]);
       
       
     // hallamos el mensaje en numeros
     //cout<<" mensaje en numeros: ";
     for(int i=0;i<tam;i++)
       {
	   	mensaje_int[i*2] = mensaje_cifrado[i]/100;
        mensaje_int[i*2+1] = mensaje_cifrado[i]%100;
       } 
     for(int i=0;i<(tam*2);i++)
         printf("%c   ",mensaje_int[i]);
   
   
     // hallamos el mensaje
     puts(" mensaje : ");
     
     for(int i=0;i<(tam*2);i++)
       mensaje+=alfabeto[mensaje_int[i]%26]);
     
	 puts(mensaje);  
      
}

void encriptar()
{
     long int p,q,n,fi,e,d;
     string mensaje,mensaje_valido;
     char mensaje_aux[300];
       cout<<" ENCRIPTAR :\n\n";
    // Debemos seguir una serie de pasos para generar las claves publica y privada :
     
    /* 1) Generamos aleatoriamente dos enteros p y q (p y q pueden ser cualquier numero
         pero deben de ser del mismo tamaño , en este caso yo quiero que sean de 2 cifras) ,
          ademas deben de ser primos */
         do
         {p=rand()%50+50;
         }while(!es_primo(p));
          
         do
         {q=rand()%50+50;
         }while(!es_primo(q));
         p=2357;
         q=2551;
         cout<<" p : "<<p<<"\n q : "<<q;
          
    /* 2) Calculamos el valor de n */
         n=p*q;
         cout<<"\n n : "<<n;
     
     
    /* 3) Calculamos el valor de fi */
         fi=(p-1)*(q-1);
         cout<<"\n fi : "<<fi;     
     
    /* 4) Seleccionamos aleatoriamente un entero 'e' tal que mcd(e,fi)=1 y 1 < e < fi */
       do{
       e=rand()%(fi-2)+2;
       }while(alg_euc(e,fi)!=1);
       cout<<"\n e : "<<e;
        
    /* 5) Usar el algoritmo de euclides extendido para hallar un entero 'd' tal que 
           ed = 1 (mod fi) donde 1 < d < fi (en otras palabras, hallar el inverso de 'e') */ 
         d=Inverso_Zn(e,fi);    
         cout<<"\n d : "<<d;  
     
     /*  6) La clave publica es (n,e) y la clave privada es d */
         cout<<"\n\n clave publica : ("<<n<<" , "<<e<<")";
         cout<<"\n clave privada : "<<d<<endl<<endl;
      
    /////////////////////////////////////////////////// 
 
     cout<<" Mensaje a encriptar : ";
     fflush(stdin);
     gets(mensaje_aux);
     mensaje=mensaje_aux;
       cout<<" mensaje : "<<mensaje<<endl;    
     mensaje_valido=validar_mensaje(mensaje);
       cout<<" mensaje valido : "<<mensaje_valido<<endl;
      
     // representamos numericamente el mensaje     
       cout<<" mensaje en numeros : ";
     long int mensaje_int[mensaje_valido.size()]; /*posiciones de los caracteres en el alfabeto del mensaje*/
     long int mensaje_cifrado[mensaje_valido.size()/2]; 
      
     for(int i=0;i<mensaje_valido.size();i++)
       mensaje_int[i]=get_pos(alfabeto,mensaje_valido.at(i));
     for(int i=0;i<mensaje_valido.size();i++)
       cout<<mensaje_int[i]<<" ";
     cout<<endl;
     cout<<" mensaje en numeros 2: ";
      
     // agrupamos de 2 en 2 el mensaje numerico
      for(int i=0;i<(mensaje_valido.size()/2);i++)
        mensaje_cifrado[i]=mensaje_int[i*2]*100+mensaje_int[i*2+1];
     for(int i=0;i<(mensaje_valido.size()/2);i++)
        cout<<mensaje_cifrado[i]<<" ";
      cout<<endl;
       
      cout<<" mensaje cifrado : ";
      // elevamos al cuadrado el mensaje_cifrado
      for(int i=0;i<(mensaje_valido.size()/2);i++)
        mensaje_cifrado[i]=Exponenciacion_Zn(mensaje_cifrado[i],e,n);
      for(int i=0;i<(mensaje_valido.size()/2);i++)
        cout<<mensaje_cifrado[i]<<" ";
      cout<<endl;      
}
 
long  Adicion_Zn(int a,int b,int n)
{
 long adicion;
 if(a+b<n)
  adicion=a+b;
 else
  adicion=a+b-n;
 return adicion;
}

//Metodo para buscar si un número es primo.
//Valido para valores chicos de n.
//Para valores reales usados en RSA (200 digitos o más) este método es inviable.
//Optimizar usando test de primaridad más avanzados.
bool es_primo(int n)
{
  int i;	
  for(i=2;i<n;i++)
    if(n%i==0)
     return false;
    
   return true;
}

int get_pos(char *str,char elemento)
{
	int i;
  	for(i=0;i<strlen(str);i++)
    	if(str[i]==elemento)
      		return i;
   	return -1;   
}

char* validar_mensaje(char* texto_plano)
{
  char* texto_plano_valido = {""};
  int i; 
// eliminamos los espacios del texto plano
  for(i=0;i < strlen(texto_plano);i++)
     if(texto_plano[i]!=' ')
     	strcat(texto_plano_valido,(char*)texto_plano[i]);
           
 // completamos con x al final para que sea potencia de 2
   int tam = strlen(texto_plano_valido);
   if(tam%2!=0)
    strcat(texto_plano_valido,"x");
    
 
  return texto_plano_valido;      
}

long Multiplicacion_Zn(int a,int b,int n)
{
 long mult;
 mult=(a*b)%n;
 return mult;
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

long Inverso_Zn(int a,int n)
{
  long* ptr,array[3];
  ptr=alg_euc_ext(n,a);
 
  array[0]=*ptr;
  array[1]=*(ptr+1);
  array[2]=*(ptr+2);
   
  if(array[0]!=1)
  return -1;
  else
  {
  if(array[2]<0)
   array[2]+=n;
   return array[2];
  }  
}

long* alg_euc_ext(int n1,int n2) // n1 es a y n2 es b
{   
   long array[3],x=0,y=0,d=0,x2 = 1,x1 = 0,y2 = 0,y1 = 1,q = 0, r = 0;
  if(n2==0)
  {
  array[0]=n1;
  array[1]=1; 
  array[2]=0;  
  }
  else
  {
   while(n2>0) 
      {
     q = (n1/n2); 
      r = n1 - q*n2; 
      x = x2-q*x1; 
      y = y2 - q*y1; 
      n1 = n2; 
      n2 = r; 
      x2 = x1; 
      x1 = x; 
      y2 = y1;             
      y1 = y; 
      }
      array[0] = n1;   // mcd (n1,n2)
      array[1] = x2;   // x
      array[2] = y2;   // y
    }
    return array;
}

unsigned long long  Exponenciacion_Zn(unsigned long long  a,unsigned long long  k,unsigned long long  n)
{
  // convertimos "k" a binario
   unsigned long long numero=k;
 
  unsigned long long bin[300];
  unsigned long long  ind=0;
  while(numero>=2)
  {
   bin[ind++]=numero%2;
   numero/=2;      
  }     
  bin[ind]=numero;    
  unsigned long long  tam=ind+1;
 // for(int i=0;i<tam;i++)
 // cout<<bin[i]<<endl;     
  /////////////////////////////   
      
  unsigned long long  b=1;
  if(k==0)
     return b;
   
  unsigned long long  A=a;   
  for(int i=(tam-1);i>=0;i--)
  {
    b=(b*b)%n;
    if(bin[i]==1)
    b=(A*b)%n;   
   // cout<<"b :"<<b<<endl;   
  }
 
return b;
}

