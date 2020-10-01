#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int n,i,j,a[10][10],bp;
    cout<<"Enter the number of rows and columns : "<<endl;
    cin>>n;
    cout<<"Enter the matrix : "<<endl;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            cin>>a[i][j];
        }
    }

    cout <<"The matrix you entered is : "<<endl;

    for (int i=0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            cout<< " ";
            cout<< a[i][j];
        }
        cout<<endl;
    }
    bp=(n-1)/2;
    cout<<"The Beautiful Position is : "<<bp<<","<<bp<<endl;

    return 0;
}