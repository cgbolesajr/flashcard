from django.shortcuts import render


# Create your views here.
def homePage(request):
    return render(request, 'website/home.html',{})


def aboutPage(request):
    return render(request, 'website/about.html',{})

def addPage(request):
    from random import randint
    num_1 = randint(1,10)
    num_2 = randint(1,10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) + int(old_num_2)


        if answer == "":
            my_answer = 'Please input your answer'
            color = 'dark'
            return render(request, 'website/add.html',{
                        "num_1":num_1,
                        "num_2":num_2,
                        'my_answer':my_answer,
                        'color':color,
            })

        if int(answer) == correct_answer:
            my_answer = 'Correct!' + old_num_1 + "+" + old_num_2 + "=" + answer
            color = 'success'


        elif int(answer) != correct_answer:
            my_answer = 'Incorrect!'+ old_num_1 + "+" + old_num_2 + "=" + str(correct_answer)
            color = 'danger'

        return render(request, 'website/add.html',{
                                                   'answer':answer,
                                                   'my_answer':my_answer,
                                                   "num_1":num_1,
                                                   "num_2":num_2,
                                                   'color':color,
                                })


    return render(request, 'website/add.html',{
                "num_1":num_1,
                "num_2":num_2
    })

def subtractPage(request):
    from random import randint
    num_1 = randint(1,10)
    num_2 = randint(1,10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) - int(old_num_2)


        if answer == "":
            my_answer = 'Please input your answer'
            color = 'dark'
            return render(request, 'website/subtract.html',{
                        "num_1":num_1,
                        "num_2":num_2,
                        'my_answer':my_answer,
                        'color':color,
            })

        if int(answer) == correct_answer:
            my_answer = 'Correct!' + old_num_1 + "-" + old_num_2 + "=" + answer
            color = 'success'


        elif int(answer) != correct_answer:
            my_answer = 'Incorrect!'+ old_num_1 + "-" + old_num_2 + "=" + str(correct_answer)
            color = 'danger'

        return render(request, 'website/subtract.html',{
                                                   'answer':answer,
                                                   'my_answer':my_answer,
                                                   "num_1":num_1,
                                                   "num_2":num_2,
                                                   'color':color,
                                })


    return render(request, 'website/subtract.html',{
                "num_1":num_1,
                "num_2":num_2
    })

def multiplyPage(request):
        from random import randint
        num_1 = randint(1,10)
        num_2 = randint(1,10)
        if request.method == 'POST':
            answer = request.POST['answer']
            old_num_1 = request.POST['old_num_1']
            old_num_2 = request.POST['old_num_2']
            correct_answer = int(old_num_1) * int(old_num_2)


            if answer == "":
                my_answer = 'Please input your answer'
                color = 'dark'
                return render(request, 'website/multiply.html',{
                            "num_1":num_1,
                            "num_2":num_2,
                            'my_answer':my_answer,
                            'color':color,
                })

            if int(answer) == correct_answer:
                my_answer = 'Correct!' + old_num_1 + "*" + old_num_2 + "=" + answer
                color = 'success'


            elif int(answer) != correct_answer:
                my_answer = 'Incorrect!'+ old_num_1 + "*" + old_num_2 + "=" + str(correct_answer)
                color = 'danger'

            return render(request, 'website/multiply.html',{
                                                       'answer':answer,
                                                       'my_answer':my_answer,
                                                       "num_1":num_1,
                                                       "num_2":num_2,
                                                       'color':color,
                                    })


        return render(request, 'website/multiply.html',{
                    "num_1":num_1,
                    "num_2":num_2
                    })



def dividePage(request):
            from random import randint
            num_1 = randint(1,10)
            num_2 = randint(1,10)
            if request.method == 'POST':
                answer = request.POST['answer']
                old_num_1 = request.POST['old_num_1']
                old_num_2 = request.POST['old_num_2']
                correct_answer = int(old_num_1) / int(old_num_2)


                if answer == "":
                    my_answer = 'Please input your answer'
                    color = 'dark'
                    return render(request, 'website/divide.html',{
                                "num_1":num_1,
                                "num_2":num_2,
                                'my_answer':my_answer,
                                'color':color,
                    })

                if float(answer) == correct_answer:
                    my_answer = 'Correct!' + old_num_1 + "/" + old_num_2 + "=" + answer
                    color = 'success'


                elif float(answer) != correct_answer:
                    my_answer = 'Incorrect!'+ old_num_1 + "/" + old_num_2 + "=" + str(correct_answer)
                    color = 'danger'

                return render(request, 'website/divide.html',{
                                                           'answer':answer,
                                                           'my_answer':my_answer,
                                                           "num_1":num_1,
                                                           "num_2":num_2,
                                                           'color':color,
                                        })


            return render(request, 'website/divide.html',{
                        "num_1":num_1,
                        "num_2":num_2
                        })
