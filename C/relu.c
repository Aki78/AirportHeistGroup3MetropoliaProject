#include "relu.h"

double relu(double x){
    if (x > 0){
        return x;
    }
    else{
        return 0;
    }

}
