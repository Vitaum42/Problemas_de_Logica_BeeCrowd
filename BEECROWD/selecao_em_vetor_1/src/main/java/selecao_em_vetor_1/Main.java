package selecao_em_vetor_1;
/* 1174 - Seleção em Vetor I
Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

Entrada
A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

Saída
Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.
*/
import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner sc = new Scanner(System.in);        
        float[] a = new float[100];
        float x = 0;
        
        
        for(int i = 0; i < a.length; i++){
            
            x = sc.nextFloat();
                a[i] = x;
        }
        for(int i = 0; i < a.length; i++){
            if (a[i] <= 10){
                System.out.println("A["+i+"]" + " = " + a[i]);
            }else{
                continue;
            }
        }
    }
 
}