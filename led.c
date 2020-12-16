#include <stdio.h>
// #include <wiringPi.h>
#define LED1 15
#define LED2 16

int main()
{
    int value;
    if(wiringPiSetup() == -1)
          return 1;
    pinMode(LED1, OUTPUT)
    pinMode(LED2, OUTPUT)

    while(1)
    {
        digitalWrite(LED1,1);
        delay(1000);
        digitalWrite(LED1,0);
        delay(1000);
        digitalWrite(LED2,1);
        delay(1000);
        digitalWrite(LED2,0);
        delay(1000);
        digitalWrite(LED1,1);
        digitalWrite(LED2,1);
        delay(1000);
        digitalWrite(LED1,1);
        digitalWrite(LED2,1);
        delay(1000);
    }
    return 0;
}