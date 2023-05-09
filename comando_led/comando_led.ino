#define led 13

void setup()
{
  Serial.begin(115200);
  pinMode(led, OUTPUT);
}

void loop()
{
  if(Serial.available() > 0)
  {
    int data_received = Serial.read();
    if(data_received == '1')
    {
      digitalWrite(led, HIGH);
    }
    else if(data_received == '0')
    { 
      digitalWrite(led, LOW);
    }
  }
}
