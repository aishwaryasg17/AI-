
import java.util.Scanner;
public class SelectionSort{

	public static void main(String[] args) {
		//int arr[]={12,67,95,100,32,89};
		Scanner scn=new Scanner(System.in);
		
		System.out.print("Enter the length of array: ");
		int n=scn.nextInt();
		System.out.println("Enter the values: ");
		
		int arr[]=new int[n];
		
		for(int k=0;k<arr.length;k++)
		{
			arr[k]=scn.nextInt();
		}
		
		System.out.println("Sorted Array ");
		for(int i=0;i<arr.length;i++)
		{
			int min_pos=i;
			for(int j=i+1;j<arr.length;j++)
			{
				if(arr[min_pos]>arr[j])
				{
					min_pos=j;
				}
				
			}
			int temp=arr[min_pos];
			arr[min_pos]=arr[i];
			arr[i]=temp;
			
			
			for(int l=0;l<arr.length;l++)
			{
				System.out.print(arr[l]+" ");
				
			}
			System.out.println();
		}	
	}
}
