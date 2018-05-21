#include <string.h>
#include <stdio.h>
#include <Adafruit_NeoPixel.h>
#define PIN 6 // номер порта к которому подключен модуль

int red, green, blue;
int old_red, old_green, old_blue;
int dim = 1;
char instr;
int commaIndex, secondCommaIndex;
String red_str, green_str, blue_str;


#define count_led 1 // количество светодиодов 
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(count_led, PIN, NEO_GRB + NEO_KHZ800); //first number change does distance between colors

void setup() {
  Serial.begin(9600);
  pixels.begin();
  pixels.show(); // Устанавливаем все светодиоды в состояние "Выключено"

  Serial.print("Init\n");
}
void loop() {
  while (Serial.available() > 0) {
      red = Serial.parseInt();
      green = Serial.parseInt();
      blue = Serial.parseInt();
    
      pixels.setPixelColor(0, pixels.Color(red, green, blue)); // Назначаем для первого светодиода цвет "Зеленый"
      pixels.show();

      Serial.print("Color = #");
      Serial.print(255 - red, HEX);
      Serial.print(255 - green, HEX);
      Serial.println(255 - blue, HEX);
  }
}
