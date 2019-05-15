int Motorder_A = 10;
int Motorder_B = 9;
int Motorizq_A = 6;
int Motorizq_B = 5;
const int EchoPin = 2;
const int TriggerPin = 3;
 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Motorder_A, OUTPUT);
  pinMode(Motorder_B, OUTPUT);
  pinMode(Motorizq_A, OUTPUT);
  pinMode(Motorizq_A, OUTPUT);
  Serial.begin(9600);
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT);
}

void Moveradelante(){
  digitalWrite(Motorder_A, HIGH);
  digitalWrite(Motorder_B, LOW);
  digitalWrite(Motorizq_A, HIGH);
  digitalWrite(Motorizq_B, LOW);
}
void Moveratras(){
  digitalWrite(Motorder_A, LOW);
  digitalWrite(Motorder_B, HIGH);
  digitalWrite(Motorizq_A, LOW);
  digitalWrite(Motorizq_B, HIGH);
}
void Moverderecha(){
  digitalWrite(Motorder_A, LOW);
  digitalWrite(Motorder_B, HIGH);
  digitalWrite(Motorizq_A, HIGH);
  digitalWrite(Motorizq_B, LOW);
}
void Moverizquierda(){
  digitalWrite(Motorder_A, HIGH);
  digitalWrite(Motorder_B, LOW);
  digitalWrite(Motorizq_A, LOW);
  digitalWrite(Motorizq_B, HIGH);
}
void Stop(){
  digitalWrite(Motorder_A, LOW);
  digitalWrite(Motorder_B, LOW);
  digitalWrite(Motorizq_A, LOW);
  digitalWrite(Motorizq_B, LOW);
}

void loop(){
  int cm = ping(TriggerPin, EchoPin);
  Serial.print("Distancia: ");
  Serial.println(cm);
  delay(10);
  Moveradelante();
  delay (2000);
  Moveratras();
  delay (2000);
  Moverderecha();
  delay (2000);
  Moverizquierda();
  delay (2000);
  Stop();
  delay (2000);
  
}
int ping(int TriggerPin, int EchoPin) {
   long duration, distanceCm;
   
   digitalWrite(TriggerPin, LOW);  //para generar un pulso limpio ponemos a LOW 4us
   delayMicroseconds(4);
   digitalWrite(TriggerPin, HIGH);  //generamos Trigger (disparo) de 10us
   delayMicroseconds(10);
   digitalWrite(TriggerPin, LOW);
   
   duration = pulseIn(EchoPin, HIGH);  //medimos el tiempo entre pulsos, en microsegundos
   
   distanceCm = duration * 10 / 292/ 2;   //convertimos a distancia, en cm
   return distanceCm;
}   
