#include <Servo.h>                // Incluye la libreria Servo
char nombre[10]= "BatCar";
char velocidad = "4";//9600
char pin[5]= "0000";

Servo servo1;                    // Crea el objeto servo1 con las caracteristicas de Servo

int izqA = 5; 
int izqB = 6; 
int derA = 9; 
int derB = 10; 
int vel = 255;            // Velocidad de los motores (0-255)
int estado = 'c';         // inicia detenido

int pecho = 2;            // define el pin 2 como (pecho) para el Ultrasonido
int ptrig = 3;            // define el pin 3 como (ptrig) para el Ultrasonido
int duracion, distancia;  // para Calcular distacia

void setup()  { 
  Serial.begin(9600);    // inicia el puerto serial para comunicacion con el Bluetooth
  pinMode(derA, OUTPUT);
  pinMode(derB, OUTPUT);
  pinMode(izqA, OUTPUT);
  pinMode(izqB, OUTPUT);
  
  pinMode(pecho, INPUT);   // define el pin 2 como entrada (pecho) 
  pinMode(ptrig,OUTPUT);   // define el pin 3 como salida  (ptrig) 
  pinMode(13,OUTPUT);

  servo1.attach(11,660,1400);    // Asocia el servo1 al pin 11, define el min y max del ancho del pulso  
                                 // eso depende del fabricante del servo
} 

void loop()  { 

  if(Serial.available()>0){        // lee el bluetooth y almacena en estado
    estado = Serial.read();
  }
  if(estado=='a'){           // Boton desplazar al Frente
    analogWrite(derB, 0);     
    analogWrite(izqB, 0); 
    analogWrite(derA, vel);  
    analogWrite(izqA, vel);       
  }
  if(estado=='b'){          // Boton IZQ 
    analogWrite(derB, 0);     
    analogWrite(izqB, 0); 
    analogWrite(derA, 0);  
    analogWrite(izqA, vel);      
  }
  if(estado=='c'){         // Boton Parar
    analogWrite(derB, 0);     
    analogWrite(izqB, 0); 
    analogWrite(derA, 0);    
    analogWrite(izqA, 0); 
  }
  if(estado=='d'){          // Boton DER
    analogWrite(derB, 0);     
    analogWrite(izqB, 0);
    analogWrite(izqA, 0);
    analogWrite(derA, vel);  
  } 

  if(estado=='e'){          // Boton Reversa
    analogWrite(derA, 0);    
    analogWrite(izqA, 0);
    analogWrite(derB, vel);  
    analogWrite(izqB, vel);      
  }
  
  if (estado =='f'){               // Boton ON,  se mueve sensando distancia 
  
     digitalWrite(ptrig, HIGH);   // genera el pulso de trigger por 10us
     delay(0.01);
     digitalWrite(ptrig, LOW);
     
     duracion = pulseIn(pecho, HIGH);          // Lee el tiempo del Echo
     distancia = (duracion/2) / 29;            // calcula la distancia en centimetros
     delay(10); 
     
     if (distancia <= 15 && distancia >=2){    // si la distancia es menor de 15cm
        digitalWrite(13,HIGH);                 // Enciende LED
        
        analogWrite(derB, 0);             // Parar los motores por 200 mili segundos
        analogWrite(izqB, 0); 
        analogWrite(derA, 0);    
        analogWrite(izqA, 0); 
        delay (200);
        
        analogWrite(derB, vel);          // Reversa durante 500 mili segundos
        analogWrite(izqB, vel); 
        delay(500);           
        
        analogWrite(derB, 0);            // Girar durante 600 milisegundos   
        analogWrite(izqB, 0); 
        analogWrite(derA, 0);  
        analogWrite(izqA, vel);  
        delay(600);
        
        digitalWrite(13,LOW);
     }
     else{                             // Si no hay obstaculos se desplaza al frente  
         analogWrite(derB, 0);     
         analogWrite(izqB, 0); 
         analogWrite(derA, vel);  
         analogWrite(izqA, vel); 
     }
  }
  if(estado=='g'){                   // Boton SER, activa el Servomotor
    servo1.write(30);                // Gira el servo a 30 grados  
    delay(1000);                     // Espera 1000 mili segundos a que el servo llegue a la posicion

    servo1.write(90);                // Gira el servo a 90 grados  
    delay(700);                      // Espera 700 mili segundos a que el servo llegue a la posicion 
 
    servo1.write(150);               //Gira el servo a 150 grados 
    delay(700);  
  }

    if(estado=='h'){                 //Programacion de los botones 13-10-9-6-5
    digitalWrite(13,1);        
  }
      if(estado=='m'){           
    digitalWrite(13,0);        
  }
    if(estado=='i'){           
    digitalWrite(derB,1);        
  }
    if(estado=='n'){           
    digitalWrite(derB,0);        
  }
    if(estado=='j'){           
    digitalWrite(derA,1);        
  }
    if(estado=='o'){           
    digitalWrite(derA,0);        
  }
    if(estado=='k'){           
    digitalWrite(izqB,1);        
  }
    if(estado=='p'){           
    digitalWrite(izqB,0);        
  }
    if(estado=='l'){           
    digitalWrite(izqA,1);        
  }
    if(estado=='q'){           
    digitalWrite(izqA,0);        
  }
  
}
