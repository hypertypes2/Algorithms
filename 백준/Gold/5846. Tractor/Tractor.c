#include <stdio.h>
#include <string.h>
#include <math.h>
#define INF (1e9)
#define MAXN (500)
int N, D, M, max, min = INF;

int grids[MAXN+10][MAXN+10];
char visit[MAXN+10][MAXN+10];
int dx[] = {-1,0,1,0};
int dy[] = {0,-1,0,1};

typedef struct {
	int x, y;
}QUE;

QUE que[MAXN*MAXN+10];

int BFS(int x, int y) 
{
	int nx, ny, front = 0,pop,cnt;
	pop=cnt=1;
	que[front].x = x;
	que[front].y = y;
	visit[y][x] = 1;

	while (1)
    {
		x = que[front].x;
		y = que[front].y;
		for (int i = 0; i < 4; i++)
		{
			nx = x + dx[i];
			ny = y + dy[i];
			if (ny < 1 || nx < 1 || nx > N || ny>N || visit[ny][nx] == 1) {continue;}
			if (grids[y][x] - grids[ny][nx] > D || grids[ny][nx]-grids[y][x] > D) {continue;}

			visit[ny][nx] = 1;
			cnt++;
			if (cnt >= M) {return cnt;}
			que[pop].x = nx;
			que[pop].y = ny;
			pop++;
			pop %= MAXN*MAXN;
		}

		front++;
		front %= MAXN*MAXN;
		if (front == pop) {return cnt;}
	}

}

int solve(void) 
{
	int i, j, result;
	for (i=1; i<=N; i++) 
    {
		for (j=1; j<=N; j++) 
        {
			if (visit[i][j] == 0) 
            {
				result = BFS(j, i);
				if (result >= M) {return 1;}
			}
		}
	}
	return 0;
}


int main(void) 
{
	int i, j, temp, ans;
	scanf("%d", &N);
	if (N*N%2 == 0) {M=N*N/2;}
	else {M = N*N/2 + 1;}

	for (i = 1; i <= N; i++)
	{
		for (j = 1; j <= N; j++)
		{
			scanf("%d", &grids[i][j]);
			if (grids[i][j] > max) 
			{
				max = grids[i][j];
			}
			else if (grids[i][j] < min) 
			{
				min = grids[i][j];
			}
		}
	}

    int s,e;
	s = 0;
	e = max - min + 1;
	ans = -1;
	while (s<=e) 
    {
		int m = (s+e)/2;
		D = m;
		temp = solve();
		memset(visit, 0, sizeof(visit));
		if (temp == 0) {s = m + 1;}
		else if (temp == 1) 
        {
			e = m-1;
			ans = m;
		}
	}
	printf("%d", ans);
	return 0;
}