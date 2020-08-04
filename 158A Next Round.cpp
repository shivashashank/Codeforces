#include<iostream>
using namespace std;

int main()
{
    int count = 0, n, k, a[100];
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (a[i] > 0 && a[i] >= a[k - 1])
        {
            count += 1;
        }
    }
    cout << count << endl;
}