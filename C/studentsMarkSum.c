#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
  int cont;
  int somaf = 0;
  int somam = 0;
  for(cont =0 ; cont<number_of_students;cont++){
      if (cont%2==0) {
        somam += marks[cont];
      }else{
          somaf+=marks[cont];
      }
  }
  if(gender == 'g'){
      return somaf;
    }else{
        return somam;
    }
  return 0;
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}
