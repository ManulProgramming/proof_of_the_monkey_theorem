from random import randint
print("""Monkey Theorem states that in an infinite amount of time, the monkey that is sitting by the typewriter, pressing random keys, will eventually write the full text for Hamlet (or whatever, it doesn't really matter) without any mistakes.
The key factor here is infinity.
Infinite time also means that there will be an infinite amount of key presses, in other words, experiments.
And we can prove, that after an infinite amount of experiments, the "probability" will become "distribution" among all the results of all the experiments.

Let's take a simple example - a coin flip.
There is a 50% chance that it will land on heads and a 50% chance that it will land on tails.
We can replace a coin flip with a random number generator from 1 to 2 inclusively.
It will still be a 50/50 chance, it is just simpler to represent in Python.
So, let's say we start generating a random integer number from 1 to 2 inclusively and write down the results in the list.
We would then see the distribution of ones in that list.
However, the distribution will vary depending on the amount of experiments. (Also as the randomness takes place here, extreme results like all ones or all twos in for example 10,000 experiments are possible and will hugely affect the research as a whole. But this is mostly taken care of, that will be later explained)
So, as an example, let's say we only generate one number and put it in the list. The list will contain only one 1 or 2, nothing more. So the distribution of ones in that list will be either 100% or 0%, which is nowhere near close to a percentage chance of 50%.
But if we increase the amount of experiments and generate more and more numbers, this distribution will get closer and closer to the 50% we need.""")
print("""Here is how it works:
	1. Define how many experiments we want, for example - 1. This will be our N number.
	2. Create a list with a length of N full of random numbers from 1 to 2 inclusively.
	3. Count how many ones are in that list, and divide the amount by the N (total amount of elements in that list) to find the distribution.
	4. Calculate the deviation of distribution from probability by using the formula:
		|probability - distribution|
	5. REPEAT the 2-4 steps approximately 1000 times (M times) to remove any extreme results, the bigger amount of repeats the better. WHY IT IS OKAY TO DO THAT:
		The extreme results are the most unlikely cases when generating random numbers, which actually become IMPOSSIBLE when dealing with an infinite amount of experiments.
		The best example of an extreme result is all the ones in the list of N experiments.
		This is so unlikely, but POSSIBLE when N is not infinite because the probability of it happening is 50%^N or 1/(2^N).
		As the number N increases, the lower the probability of it happening, and when it reaches infinity, it will just become 0%, because 1/(2^infinity) is 1/infinity which is 0.
		But if N is some kind of integer, then this case becomes possible, even in 10,000 experiments, as it will be more than 0% -> 1/(2^10000) ~ 5.0124e-3011.
		So to not ruin our research, we can just avoid those extreme results, by repeating the steps of generating those numbers, and then calculating the average deviation of all of the deviations we calculated, by doing so we will receive an actual deviation of the experiments.
	6. Calculate the average deviation of all deviations received from the repeating process.

This is how the algorithm works, let's see how it works in practice (it might take some time because of the repetition and the creation of a list with N random numbers):""")
should_we=input("Run the code? (y/n) ").lower()
if should_we=='y':
    for n in range(1,10002,1000):
        m=1000
        from_what_random=1
        to_what_random=2
        mean_of_experiments=sum([abs((from_what_random/to_what_random * 100) - [randint(from_what_random,to_what_random) for _ in range(n)].count(from_what_random)/n * 100) for _ in range(m)])/m
        print(f"n={n}: {from_what_random/to_what_random * 100}% ± {mean_of_experiments}%")
else:
    print("""The results from the saved running process:
n=1: 50.0% ± 50.0%
n=1001: 50.0% ± 1.199800199800202%
n=2001: 50.0% ± 0.8891054472763642%
n=3001: 50.0% ± 0.7411196267910696%
n=4001: 50.0% ± 0.6420644838790304%
n=5001: 50.0% ± 0.5564487102579485%
n=6001: 50.0% ± 0.5087152141309798%
n=7001: 50.0% ± 0.4636337666047699%
n=8001: 50.0% ± 0.45351831021122346%
n=9001: 50.0% ± 0.42366403732918495%
n=10001: 50.0% ± 0.39894010598940083%""")

print("""
As you can see, the bigger the number N, the lower the average deviation of the percentage of the distribution.
So, if N reaches infinite, the average deviation will become 0, and the distribution of ones in the list will be equal to the chance of 1 happening in the random number generator.
And what it gets us is that in an infinite amount of experiments, 50% of all of those experiments will be ones. In other words, there is a 100% chance that there is at least one 1 in the infinite amount of experiments of generating a random number from 1 to 2 inclusively.

We can also test this with the example from the Monkey Theorem.
Let's say the monkey sitting by the typewriter and typing random uppercase English letters after infinite time will eventually type the word "ONCE".
To prove it, we must first calculate the probability of it happening. So, the formula of it's happening is 1/(26^4), where
26 - is the amount of uppercase English letters in the alphabet,
4 - is the amount of letters in the word "ONCE".
By calculating the probability we will get: 0.00021882987290360983%, which is unlikely, but possible.

This experiment can be once again represented by the random number generator, but this time from 1 to 26^4 (456976) inclusively.
(The code once again will take more time than the previous example, because the lists will be bigger in size. To optimize it at least by some amount in cost of accuracy, the repetition amount M is decreased to 50).""")
should_we=input("Run the code? (y/n) ").lower()
if should_we=='y':
    for n in range(100000,1000001,100000):
        m=50
        from_what_random=1
        to_what_random=456976
        mean_of_experiments=sum([abs((from_what_random/to_what_random * 100) - [randint(from_what_random,to_what_random) for _ in range(n)].count(from_what_random)/n * 100) for _ in range(m)])/m
        print(f"n={n}: {from_what_random/to_what_random * 100}% ± {mean_of_experiments}%")
else:
    print("""n=100000: 0.00021882987290360983% ± 0.0004025447288260213%
n=200000: 0.00021882987290360983% ± 0.00026877875424529925%
n=300000: 0.00021882987290360983% ± 0.00020793903107967725%
n=400000: 0.00021882987290360983% ± 0.00019249361016771116%
n=500000: 0.00021882987290360983% ± 0.00015327236441301084%
n=600000: 0.00021882987290360983% ± 0.00017043264124738867%
n=700000: 0.00021882987290360983% ± 0.00015288270218629795%
n=800000: 0.00021882987290360983% ± 0.00014500000000000006%
n=900000: 0.00021882987290360983% ± 0.00010249361016771117%
n=1000000: 0.00021882987290360983% ± 0.00012501277966457758%""")
print("""
While not exactly noticeable and accurate as in the previous example, we can still determine that the more experiments we have the more equal distribution will be to the probability.
So we can say that in the infinite amount of experiments, 0.00021882987290360983% of them are the word "ONCE". Judging by it, we can 100% guarantee that in infinite attempts (experiments or time) the monkey will at least once write the word "ONCE".
This is the same case with every single 4 character English word, and also the same with every single word, sentence, text, whatever. Even if the longer the word/sentence/text is, the lower the probability and so is the distribution, it is still guaranteed to happen at least once in the infinite amount of attemps.
But of course, this is not the case with infinite texts/strings, that only contain an endless repetition of one character, as it will be a 0% chance of happening, as proven before when discussing extreme results.""")
