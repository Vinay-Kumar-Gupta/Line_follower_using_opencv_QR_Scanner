#include <cvzone.h>

SerialData serialData(2, 3);

int motor_vals[2];

int in1 = 13;
int in2 = 12;
int in3 = 14;
int in4 = 27;

int en1 = 25;
int en2 = 26;

int value1;
int value2;

void setup() {

  serialData.begin();
  Serial.begin(9600);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);

  digitalWrite(en1, HIGH);
  digitalWrite(en2, HIGH);
}

void forward(int value1, int value2) {
  //   digitalWrite(en1,HIGH);
  // digitalWrite(en2,HIGH);
  analogWrite(en1, value1);
  analogWrite(en2, value2);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void backward(int value1, int value2) {
  //   digitalWrite(en1,HIGH);
  // digitalWrite(en2,HIGH);
  analogWrite(en1, value1);
  analogWrite(en2, value2);
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}

void left(int value1, int value2) {
  //   digitalWrite(en1,HIGH);
  // digitalWrite(en2,HIGH);
  analogWrite(en1, value1);
  analogWrite(en1, value2);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}

void right(int value1, int value2) {
  //   digitalWrite(en1,HIGH);
  // digitalWrite(en2,HIGH);
  analogWrite(en1, value1);
  analogWrite(en2, value2);
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void stop() {
  digitalWrite(en1, LOW);
  digitalWrite(en2, LOW);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}


void loop() {
  serialData.Get(motor_vals);
  Serial.print(motor_vals[0]);
  Serial.println(motor_vals[1]);
  forward(motor_vals[0], motor_vals[1]);
  // delay(1000);
}
