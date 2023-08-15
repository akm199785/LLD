Strategy is behavioral design pattern that let you define family of algorithm and put each of them into separate class and make them their object interchangeable


Applicability

1. Use the Strategy when you want to use different varient of an algorithms within an object and be able to swith from one algo to another at runtime

2. Use the Strategy when you have a lot of similar classes that only differ in way they exicute some behaviour 

3. Use the pattern when your class has a massive conditional statement that switches between different variants of the same algorithm.

4. Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.

How to Implement


In the context class, identify an algorithm that’s prone to frequent changes. It may also be a massive conditional that selects and executes a variant of the same algorithm at runtime.

Declare the strategy interface common to all variants of the algorithm.

One by one, extract all algorithms into their own classes. They should all implement the strategy interface.

In the context class, add a field for storing a reference to a strategy object. Provide a setter for replacing values of that field. The context should work with the strategy object only via the strategy interface. The context may define an interface which lets the strategy access its data.

Clients of the context must associate it with a suitable strategy that matches the way they expect the context to perform its primary job.