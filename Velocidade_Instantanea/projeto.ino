//biblioteca do lcd
#include <LiquidCrystal_I2C.h>

//variaveis dos sensores óptico
int sensor_um = 33;
int sensor_dois = 32;
int sensor_tres = 26;
int sensor_quatro = 27;

LiquidCrystal_I2C lcd(0x27, 16, 2);
//flag para cada sensor
int valorUm, valorDois, valorTres, valorQuatro = 0;

void setup() {
  lcd.init();  //iniciando o lcd
  lcd.backlight();
  //informando se o pino é entrada ou saida
  pinMode(sensor_um, INPUT);
  pinMode(sensor_dois, INPUT);
  pinMode(sensor_tres, INPUT);
  pinMode(sensor_quatro, INPUT);
  //mudando velocidade do serial
  Serial.begin(9600);
}
void loop() {
  //guardando a leitura dos sensores ópticos
  valorUm = 0;
  valorDois = 0;
  valorTres = 0;
  valorQuatro = 0;

  while (valorUm == 0) {
    if (digitalRead(sensor_um) == LOW) {
      lcd.setCursor(0, 0);
      lcd.print("1:");
      lcd.println(millis());
      valorUm = 1;
    }
  }

  while (valorDois == 0) {
    if (digitalRead(sensor_dois) == LOW) {
      lcd.setCursor(8, 0);
      lcd.print("2:");
      lcd.println(millis());
      valorDois = 1;
    }
  }

  while (valorTres == 0) {
    if (digitalRead(sensor_tres) == LOW) {
      lcd.setCursor(0, 1);
      lcd.print("3:");
      lcd.println(millis());
      valorTres = 1;
    }
  }

  while (valorQuatro == 0) {
    if (digitalRead(sensor_quatro) == LOW) {
      lcd.setCursor(8, 1);
      lcd.print("4:");
      lcd.println(millis());
      valorQuatro = 1;
    }
  }
}