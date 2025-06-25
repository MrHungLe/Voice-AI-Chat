#define MAX 40
#include<stdio.h>
#include<string.h>

typedef struct{
    char MSSV[10];
    char HoTen[50];
    float DiemLT;
    float DiemTH1;
    float DiemTH2;
}SinhVien;
typedef struct{
    SinhVien A[MAX];
    int n;
    
}DanhSach;
void  hienthiDat(DanhSach L){
    float tong;
    for(int i=0; i<L.n; i++){
        SinhVien sv = L.A[i];
        tong = sv.DiemLT + sv.DiemTH1 + sv.DiemTH2;
        if(tong >= 4.0){
            printf("%s - ", sv.MSSV);
            printf("%s - ", sv.HoTen);
            printf("%.2f - ", sv.DiemLT);
            printf("%.2f - ", sv.DiemTH1);
            printf("%.2f - ", sv.DiemTH2);
            printf("%.2f\n", tong);
        }
    }
}
int main(){
    DanhSach L;
    scanf("%d", &L.n);
    for(int i=0; i<L.n; i++){
        scanf("%s", L.A[i].MSSV);
        fgets(L.A[i].HoTen, sizeof(L.A[i].HoTen), stdin);
        L.A[i].HoTen[strcspn(L.A[i].HoTen, "\n")] = '\0';
        scanf("%f", &L.A[i].DiemLT);
        scanf("%f", &L.A[i].DiemTH1);
        scanf("%f", &L.A[i].DiemTH2);
    }
    hienthiDat(L);
    return 0;
}
