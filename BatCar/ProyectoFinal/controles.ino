#include <Servo.h>                // Incluye la libreria Servo
Servo servo1;                    // Crea el objeto servo1 con las caracteristicas de Servo

int izqA = 5; 
int izqB = 6; 
int derA = 9; 
int derB = 10; 
int vel = 255;            // Velocidad de los motores (0-255)
int estado = 'c';
void setup() {
  Serial.begin(9600);    // inicia el puerto serial para comunicacion con el Bluetooth
  pinMode(derA, OUTPUT);
  pinMode(derB, OUTPUT);
  pinMode(izqA, OUTPUT);
  pinMode(izqB, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
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
  if(estado=='g'){                   // Boton SER, activa el Servomotor
    servo1.write(30);                // Gira el servo a 30 grados  
    delay(1000);                     // Espera 1000 mili segundos a que el servo llegue a la posicion

    servo1.write(90);                // Gira el servo a 90 grados  
    delay(700);                      // Espera 700 mili segundos a que el servo llegue a la posicion 
 
    servo1.write(150);               //Gira el servo a 150 grados 
    delay(700); 
  }
}
