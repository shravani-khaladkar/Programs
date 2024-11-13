/*
Name: SHRAVANI KHALADKAR
Roll No.: 35
PRN - F23112040
Class: SE Comp 2
Batch - Q
*/

/*
Problem Statement:
Pizza parlor accepting maximum M orders. Orders are served in first come first served basis. 
Order once placed cannot be cancelled. 
Write C++ program to simulate the system using circular queue using array.
*/

#include <iostream>
using namespace std;

#define size 5

class pizza
{
    int porder[size];
    int front, rear;

public:
    pizza()
    {
        front = rear = -1;
    }
    int qfull()
    {
        if (front == (rear + 1) % size)
            return 1;
        else
            return 0;
    }
    int qempty()
    {
        if (front == -1)
            return 1;
        else
            return 0;
    }
    void accept_order(int item)
    {
        if (qfull())
            cout << "\nVery Sorry !!!! No more orders....\n";
        else
        {
            if (front == -1)
            {
                front = rear = 0;
            }
            else
            {
                rear = (rear + 1) % size;
            }
            porder[rear] = item;
        }
    }
    void make_payment(int n)
    {
        int item;
        char ans;
        if (qempty())
            cout << "\nSorry !!! order is not there...\n";
        else
        {
            cout << "\nDeliverd orders as follows...\n";
            for (int i = 0; i < n; i++)
            {
                item = porder[front];
                if (front == rear)
                {
                    front = rear = -1;
                }
                else
                {
                    front = (front + 1) % size;
                }
                cout << "\t" << item;
            }
            cout << "\nTotal amount to pay : " << n * 100;
            cout << "\nThank you visit Again....\n";
        }
    }
    void order_in_queue()
    {
        int temp;
        if (qempty())
        {
            cout << "\nSorry !! There is no pending order...\n";
        }
        else
        {
            temp = front;
            cout << "\nPending Order as follows..\n";
            while (temp != rear)
            {
                cout << "\t" << porder[temp];
                temp = (temp + 1) % size;
            }
            cout << "\t" << porder[temp];
        }
    }
};

int main()
{
    pizza p1;
    int ch, k, n;
    do
    {
        cout << "\n\t***** Welcome To Pizza Parlor *******\n";
        cout << "\n1.Accept order\n2.Make_payment\n3.Pending Orders\nEnter u r choice:";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "\nWhich Pizza would do u like to have today\n";
            cout << "\n1.Veg Soya Pizza\n2.Veg butter Pizza\n3.Egg_Pizza";
            cout << "\nPlease enter your order: ";
            cin >> k;
            p1.accept_order(k);
            break;
        case 2:
            cout << "\nHow many Pizza ?";
            cin >> n;
            p1.make_payment(n);
            break;
        case 3:
            cout << "\n Following orders are in queue to deliver....as follows..\n";
            p1.order_in_queue();
            break;
        }
    } while (ch != 4);

    return 0;
}

/*
OUTPUT:
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 1
Enter order number to add: 0
Order 0 added to the queue.
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 1
Enter order number to add: 1
Order 1 added to the queue.
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 1
Enter order number to add: 2
Order 2 added to the queue.
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 1
Enter order number to add: 3
Order 3 added to the queue.
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 1
Enter order number to add: 4
Order 4 added to the queue.
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 1
Enter order number to add: 5
Queue is full. Cannot take more orders.
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 2
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 3
Orders in the queue: 1 2 3 4
1. Add Order
2. Serve Order
3. Display Orders
4. Exit
Enter your choice: 4
Exiting...
*/