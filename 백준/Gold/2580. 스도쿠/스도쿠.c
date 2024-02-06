#include <stdio.h>
#define MAXN (9)
int sudoku[MAXN][MAXN];
int table[9];
int task_size=0;

struct QUE {
    int r, c;
};

struct QUE que[10*10*100];
int wp,rp;
void push(int r, int c) {
    que[wp].r = r; que[wp].c = c; wp++;
}

int size(void) {return wp-rp;}

int local(int r, int c,int num)
{
    for (int i=table[r];i<table[r]+3;i++)
    {
        for (int j=table[c];j<table[c]+3;j++)
        {
            if (sudoku[i][j]==num){return 0;}
        }
    }
    return 1;
}

int global(int r, int c, int num)
{
    for (int i=0;i<MAXN;i++)
    {
        if (sudoku[r][i]==num || sudoku[i][c]==num){return 0;}
    }
    return 1;
}

int flag=0;
void DFS(int task)
{   
    if (flag==1){return;}
    if (task==task_size)
    {
        for (int r=0; r<MAXN; r++)
        {
            for (int c=0; c<MAXN; c++)
            {
                printf("%d ", sudoku[r][c]);
            }
        printf("\n");
        }
        flag=1;
    }   
    else
    {
		int nr = que[task].r;
		int nc = que[task].c;
		for (int num=1; num<=MAXN; num++) 
		{
			if (global(nr,nc,num)==1 && local(nr,nc,num)==1)
			{
				sudoku[nr][nc] = num;
				DFS(task+1);
				sudoku[nr][nc] = 0;        
            }
		}
    }
}

void setup()
{
    wp=rp=0;
    for (int i=0;i<MAXN;i++)
    {
        for (int j=0;j<MAXN;j++)
        {
            if (sudoku[i][j]==0)
            {
                push(i,j);
            }
        }
    }
    
    task_size=size();
    //printf("%d\n",task_size);
    
    for (int i=0;i<MAXN;i++)
    {
        table[i]=3*(i/3);
    }
    
    //DFS(0);
}


void InputData(void){
    for (int r=0; r<MAXN; r++){
        for (int c=0; c<MAXN; c++){
            scanf("%d", &sudoku[r][c]);
        }
    }
}
void OutputData(void){
    for (int r=0; r<MAXN; r++){
        for (int c=0; c<MAXN; c++){
            printf("%d ", sudoku[r][c]);
        }
        printf("\n");
    }
}
int main(void){
    InputData();
    setup();
    DFS(0);
    //OutputData();
    return 0;
}