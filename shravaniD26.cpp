/*
Name: SHRAVANI KHALADKAR
Roll No.: 35
PRN - F23112040
Class: SE Comp 2
Batch - Q
*/

/*
Problem Statement:
In any language program mostly syntax error occurs due to unbalancing delimiter such as (),{},[]. 
Write C++ program using stack to check whether given expression is well parenthesized or not.
*/

#include<iostream>
using namespace std;

class stack1
{
    int top;
    char stack2[100];
    char infix[100];
public:
    stack1()
    {
        top = -1;
    }
    void infix1();
    void check();
    int check1(char tkn);
    void push(int x);
    int pop();
    bool isEmpty();
    bool isFull();
    void display();
};

bool stack1::isEmpty()
{
    if(top == -1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool stack1::isFull()
{
    if(top == 100 - 1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void stack1::push(int x)
{
    if(!isFull())
    {
        top++;
        stack2[top] = x;
    }
    else
    {
        cout<<"Stack is full!!\n";
    }
}

int stack1::pop()
{
    int x;
    if(!isEmpty())
    {
        x = stack2[top];
        top--;
        return x;
    }
    else
    {
        cout<<"Stack is empty!!\n";
    }
}

int stack1::check1(char tkn)
{
    if(isEmpty())
    {
        return 0;
    }
    if(stack2[top] == '(')
    {
        if(tkn == ')')
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    if(stack2[top] == '{')
    {
        if(tkn == '}')
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    if(stack2[top] == '[')
    {
        if(tkn == ']')
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}

void stack1::check()
{
    char tkn;
    int x = 0;
    for(int i = 0; infix[i]!='\0'; i++)
    {
        tkn = infix[i];
        if(tkn == '('||tkn == ')'||tkn == '['||tkn == ']'||tkn == '{'||tkn == '}')
        {
            if(tkn == '('||tkn == '['||tkn == '{')
            {
                push(tkn);
            }
            if(tkn == '}'||tkn == ']'||tkn == ')')
            {
                x = check1(tkn);
                if(x == 1)
                {
                    pop();
                }
                else
                {
                    push(tkn);
                    break;
                }
            }
        }
    }
    if(!isEmpty())
    {
        cout<<"Equation is not paranthesized!!\n";
    }
    else
    {
        cout<<"Equation is paranthesized!!\n";
    }
}

void stack1::infix1()
{
    cout<<"\nEnter infix expression(end expression with '#'): ";
    for(int  i = 0; i < 100; i++)
    {
        cin>>infix[i];
        if(infix[i] == '#')
        {
            infix[i] = '\0';
            break;
        }
    }
}

void stack1::display()
{
    for(int  i = 0; infix[i]!= '\0'; i++)
    {
        cout<<infix[i];
    }
    cout<<"\n";
}

int main()
{
    int ch = 0;
    do
    {
        stack1 obj;
        obj.infix1();
        obj.display();
        obj.check();
        cout<<"\nDO YOU WANT TO CHECK ANOTHER EXPRESSION?\n";
        cout<<"\nEnter choice: ";
        cout<<"1(YES) \n2(NO) \n";
        cin>>ch;
    }while(ch == 1);
    return 0;
}

/*
OUTPUT:
Enter infix expression(end expression with '#'): a+(b/c)-[d*e+{x-y}]#
a+(b/c)-[d*e+{x-y}]
Equation is paranthesized!!

DO YOU WANT TO CHECK ANOTHER EXPRESSION?

Enter choice: 1(YES) 
2(NO) 
1

Enter infix expression(end expression with '#'): (x*y-d){a+[c}]#
(x*y-d){a+[c}]
Equation is not paranthesized!!

DO YOU WANT TO CHECK ANOTHER EXPRESSION?

Enter choice: 1(YES) 
2(NO) 
2
*/