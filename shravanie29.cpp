/*

Name: SHRAVANI KHALADKAR
Roll No.: 35
PRN - F23112040
Class: SE Comp 2
Batch - Q

*/

/* 
Problem Statement:
Queues are frequently used in computer programming, and a typical example is the creation of a job queue by an operating system. 
If the operating system does not use priorities, then the jobs are processed in the order they enter the system. 
Write C++ program for simulating job queue. Write functions to add job and delete job from queue.
*/

#include <iostream>
using namespace std;

class queue {
// Class for queue.

  int data[30];
  int front,rear;
  
  public:
    queue() {
    // Constructor that initialises values for front and rear. 
    front=-1;
    rear=-1;
    }

  int emptyCheck() {
  // Check if it's empty
    if (front==-1 || front>rear) {
      return 1;
    }
    else {
      return 0;
    }
  }
  
  int fullCheck() {
  // Check if it's full
    if (rear>=30) {
      return 1;
    }
    else {
      return 0;
    }
  }

  void enqueue(int x) {
  // Add job to queue
    if (fullCheck()==1) {
      cout<<endl<<"Job queue is full."<<endl;
    }
    
    else {
      if (front==-1) {
        front++;
      }
      rear++;
      data[rear]=x;
    }
  }
  
  void dequeue() {
  // Remove job from queue.
    int x;
    if (emptyCheck()) {
      cout<<endl<<"Job queue is empty."<<endl;
    }
    else {
      x=data[front];
      front++;
      cout<<endl<<"Job ["<<x<<"] has been deleted.";
    }
  }

  void display() {
  // Displaying job queue.
    cout<<"Job queue is:\t[ ";
    for (int i=front; i<=rear; i++) {
      cout<<data[i]<<" | ";
    }
    cout<<"]"<<endl;
  }
};

int main() {
// Main function
  int choice, job, totalJobs;
  queue jobQueue;
  
//Input inital jobs
  cout<<"Enter number of jobs:\t";
  cin>>totalJobs;
  for (int i=0; i<totalJobs; i++) {
   cout<<endl<<"Enter job number: \t";
   cin>>job;
   jobQueue.enqueue(job);
  }

  while (1) {
    cout<<endl<<"----- JOB QUEUE MENU -----"<<endl;
    cout<<endl<<"1 -> Add job to queue"<<endl;
    cout<<endl<<"2 -> Delete a job from queue"<<endl;
    cout<<endl<<"3 -> Display queue"<<endl;
    cout<<endl<<"4 -> Exit"<<endl;
    cout<<endl<<endl<<"Choose an option (1-4):\t";
    cin>>choice;
    
    switch (choice) {
      case 1:
        cout<<"Add additional job:\t";
        cin>>job;
        jobQueue.enqueue(job);
        cout<<"\n==============\n";
        jobQueue.display();
        cout<<"=============\n";
        break;

      case 2:
        jobQueue.dequeue();
        cout<<"\n==============\n";
        jobQueue.display();
        cout<<"=============\n";
        break;
        
      case 3:
        cout<<"\n==============\n";
        jobQueue.display();
        cout<<"=============\n";
        break;
      
      case 4:
        exit(0);
        
      default:
        cout<<endl<<"Please choose a valid option (1-4)."<<endl;
    }
  }

  return 0;
}

/* 
OUTPUT:
Enter number of jobs:	4

Enter job number: 	34

Enter job number: 	8

Enter job number: 	96

Enter job number: 	42

----- JOB QUEUE MENU -----

1 -> Add job to queue

2 -> Delete a job from queue

3 -> Display queue

4 -> Exit


Choose an option (1-4):	1
Add additional job:	77

==============
Job queue is:	[ 34 | 8 | 96 | 42 | 77 | ]
=============

----- JOB QUEUE MENU -----

1 -> Add job to queue

2 -> Delete a job from queue

3 -> Display queue

4 -> Exit


Choose an option (1-4):	2

Job [34] has been deleted.
==============
Job queue is:	[ 8 | 96 | 42 | 77 | ]
=============

----- JOB QUEUE MENU -----

1 -> Add job to queue

2 -> Delete a job from queue

3 -> Display queue

4 -> Exit


Choose an option (1-4):	3

==============
Job queue is:	[ 8 | 96 | 42 | 77 | ]
=============

----- JOB QUEUE MENU -----

1 -> Add job to queue

2 -> Delete a job from queue

3 -> Display queue

4 -> Exit

Choose an option (1-4):	4
*/
