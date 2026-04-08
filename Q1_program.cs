using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Queue<Order> orders = new Queue<Order>();

        while (true)
        {
            Console.WriteLine("\n--- Dublin Churros Shop ---");
            Console.WriteLine("1. Place an Order");
            Console.WriteLine("2. Checkout");
            Console.WriteLine("0. Exit");

            int choice = int.Parse(Console.ReadLine());

            if (choice == 1)
            {
                Console.WriteLine("1. Plain (€6)");
                Console.WriteLine("2. Cinnamon Sugar (€6)");
                Console.WriteLine("3. Chocolate Syrup (€8)");
                Console.WriteLine("4. Nutella Crunch (€8)");

                int item = int.Parse(Console.ReadLine());

                Console.Write("Quantity: ");
                int qty = int.Parse(Console.ReadLine());

                string name = "";
                double price = 0;

                if (item == 1) { name = "Plain"; price = 6; }
                else if (item == 2) { name = "Cinnamon Sugar"; price = 6; }
                else if (item == 3) { name = "Chocolate Syrup"; price = 8; }
                else if (item == 4) { name = "Nutella Crunch"; price = 8; }

                Order o = new Order(name, qty, price);
                orders.Enqueue(o);

                Console.WriteLine($"Your Order has been placed! The Order Number is {o.OrderNo}");
                Console.WriteLine($"Bill: €{o.PayBill()}");
            }
            else if (choice == 2)
            {
                if (orders.Count > 0)
                {
                    Order o = orders.Dequeue();
                    o.CollectOrder();
                }
                else
                {
                    Console.WriteLine("No orders left.");
                }
            }
            else if (choice == 0)
            {
                break;
            }
        }
    }
}
