import java.util.*;
class Student
{
	int entryno =0;
	String name;
}
class Science extends Student
{
	float physics,chemistry,mathematics;
	void read()
	{	
		entryno=1;
		Scanner s=new Scanner(System.in);
		System.out.println("enter the name");
		name=s.next();
		System.out.println("enter physics marks");
		physics=s.nextFloat();
		System.out.println("enter chemistry marks");
		chemistry=s.nextFloat();
		System.out.println("enter mathematics marks");
		mathematics=s.nextFloat();
		//return obj;
	}
	void display()
	{
		System.out.println("EntryNo="+entryno);	
		System.out.println("Name="+name);
		System.out.println("physics="+physics);
		System.out.println("chemistry="+chemistry);
		System.out.println("mathematics="+mathematics);
	}
		
	
}
class Arts extends Student
{

	float english,history,economics;
	void read()
	{	
		entryno=2;
		Scanner s=new Scanner(System.in);
		System.out.println("enter the name");
		name=s.next();
		System.out.println("enter english marks");
		english=s.nextFloat();
		System.out.println("enter history marks");
		history=s.nextFloat();
		System.out.println("enter economics marks");
		economics=s.nextFloat();
		//return obj;
	}
	
	void display()
	{
		System.out.println("EntryNo="+entryno);	
		System.out.println("Name="+name);
		System.out.println("english="+english);
		System.out.println("history="+history);
		System.out.println("economics="+economics);
	}

}
class Demo
{
	public static void main(String args[])
	{
		Science sc=new Science();
		Science sc1=new Science();
		Science sc2=new Science();
		sc.read();
		sc1.read();
		sc2.read();
		Arts ar=new Arts();
		Arts ar1=new Arts();
		ar.read();
		ar1.read();
		sc.display();
		sc1.display();
		sc2.display();
		ar.display();
		ar1.display();	
		
	}
}	
