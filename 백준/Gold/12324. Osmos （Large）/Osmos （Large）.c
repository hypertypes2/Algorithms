#include <stdio.h>
#define MAXN (100)

int A;
int N;
int W[MAXN+10];
int sol,cnt;

void sort(int s, int e)
{
    for (int i=s;i<e;i++)
    {
        for(int j=i+1;j<=e;j++)
        {
            if (W[i]>W[j])
            {
                int temp=W[i];
                W[i]=W[j];
                W[j]=temp;
            }
        }
    }
}

void DFS(int a, int n, int cnt) 
{
    if (n>=N) 
    {
        if (sol>cnt){sol=cnt;}
        return;
    }
    if (cnt >= sol) {return;}

    if (a>W[n]) 
    {
        DFS(a+W[n],n+1, cnt);
    }
    else 
    {   
        if (a!=1){DFS(a+a-1,n,cnt+1);}
        DFS(a,n+1,cnt+1);
    }
}
 

int solve(void) {
    sol = MAXN;
    DFS(A,0,0);
    return sol;
}
 
void InputData(void){
    scanf("%d %d", &A, &N);
    for (int i=0; i<N; i++){
        scanf("%d", &W[i]);
    }
}
 
int main(void){
    int t, T, ans = -1;
    scanf("%d", &T);
    for (t=1; t<=T; t++){
        InputData();
        sort(0,N-1);
        ans=solve();
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}