#include<iostream.h>
#include<stdlib.h>
#include<conio.h>
struct list
{
	int data;
	struct list *link;
};
struct list *head;
void addatend()
{
	struct list *item;
	struct list *temp=head;
	int num;
	item=new list;
	cout<<"enter";
	cin>>num;
	item->data=num;
	item->link=NULL;
	if(head==NULL)
		head=item;
	else
	{
		while(temp->link!=NULL)
			temp=temp->link;
		temp->link=item;
	}
}
void display()
{
	struct list *temp;
	temp=head;
	if(temp==NULL)
		cout<<"empty"<<endl;
	else
	{
		while(temp!=NULL)
		{
			cout<<temp->data<<"\t";
			temp=temp->link;
		}
	}
	cout<<endl;
}
int addatspepos()
{
	struct list *temp=head;
	struct list *item;
	item=new list;
	int count=0;
	int pos,num;
	cout<<"enter pos" <<endl;
	cin>>pos;
	cout<<"enter num"<<endl;
	cin>>num;
	item->data=num;
	item->link=NULL;
	if(pos==1)
	{
			item->link=head;
			head=item;
	}
	else
	{
		while(temp!=NULL)
		{
			count++;
			if(count==pos-1)
			{
				item->link=temp->link;
				temp->link=item;
				return 0;
			}
			temp=temp->link;
		}
		cout<<"the entered position doesn't exist yet\n";
	}
	return 0;
}

int addafter()
{
	struct list *temp=head;
	struct list *item;
	item=new list;
	int num_to_add,num_after;
	cout<<"enter the number to be added\n";
	cin>>num_to_add;
	cout<<"enter number after which\n the previously entered number should be added\n";
	cin>>num_after;
	item->data=num_to_add;
	item->link=NULL;
	while(temp!=NULL)
	{
		if(temp->data==num_after)
		{
			item->link=temp->link;
			temp->link=item;
			return 0;
		}
		temp=temp->link;
	}
	cout<<"the number you entered wasn't found\nso couldn't insert number\n";
	return 0;
}
int delatspepos()
{
	struct list *temp=head;
	int count=0,pos;
	cout<<"enter the position to be deleted\n";
	cin>>pos;
	if(pos==1)
		head=head->link;
	else
	{
		while(temp!=NULL)
		{
			count++;
			if(count==pos-1)
			{
				temp->link=temp->link->link;
				return 0;
			}
			temp=temp->link;
		}
		cout<<"the entered position doesn't exist \n";
	}
	return 0;
}
int delafter()
{
	struct list *temp=head;
	int num_after;
	cout<<"enter number after which the number should be deleted\n";
	cin>>num_after;
	while(temp!=NULL)
	{
		if(temp->data==num_after)
		{
			temp->link=temp->link->link;
			return 0;
		}
		temp=temp->link;
	}
	cout<<"the number you entered wasn't found\nso couldn't delete number\n";
	return 0;
}
void main()
{
	clrscr();
	addatend();
	addatend();
	addatend();
	addatend();
	addatend();
	addatend();
	addatend();
	addatend();
	addatend();
	addatend();

	display();
	delatspepos();
	display();
	delatspepos();
	display();
	getch();
}
