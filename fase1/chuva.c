#include<stdio.h>

int main() {
    int n, s;
    scanf("%d %d", &n, &s);
    int out[n];
    for(int i=0;i<n;i++) scanf("%d", &out[i]);

    int i=0,j=0;
    int saida=0;
    for(int i=0; i<n;i++){
        int soma=0;
        for(int j=i; j<n;j++){
            soma+=out[j];
            if(soma>s)break;
            if(soma == s) saida++;
        }
    }
    printf("%d\n", saida);
}
