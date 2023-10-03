
#define fechadura 3
#define led_vermelho 4
#define led_verde 5
int valor_lido;

void setup() {
  Serial.begin(9600);
  pinMode(fechadura, OUTPUT);
  pinMode(led_vermelho, OUTPUT);
  pinMode(led_verde, OUTPUT);
digitalWrite(led_vermelho,HIGH);

}

void loop() 
{

  if (Serial.available() >0) {
    valor_lido = Serial.read();
  }

  if (valor_lido == '1') {
    digitalWrite(led_vermelho,LOW);
    digitalWrite(led_verde,HIGH);
    delay(1000);
    digitalWrite(led_verde,LOW);
    digitalWrite(fechadura, HIGH);
    delay(1000);
    digitalWrite(led_vermelho,HIGH);
  } else {
    digitalWrite(fechadura, LOW);
  }
}
