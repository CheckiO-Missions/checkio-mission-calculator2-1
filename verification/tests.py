"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["000000"],
            "answer": "0",
            "explanation": "single zero instead of multi-zeros number",
        },
        {
            "input": ["0000123"],
            "answer": "123",
            "explanation": "remove beginning zeros",
        },
        {
            "input": ["12"],
            "answer": "12",
            "explanation": "you see what you enter",
        },
        {
            "input": ["+12"],
            "answer": "12",
            "explanation": "ignore beginning operations",
        },
        {
            "input": [""],
            "answer": "0",
            "explanation": "when power on - 0 on the screen",
        },
        {
            "input": ["1+2"],
            "answer": "2",
            "explanation": "last entered number, no operations after",
        },
        {
            "input": ["2+"],
            "answer": "2",
            "explanation": "single +/- do nothing",
        },
        {
            "input": ["1+2="],
            "answer": "3",
            "explanation": "standard operation",
        },
        {
            "input": ["1+2-"],
            "answer": "3",
            "explanation": "last sign requires previous calculations to be done",
        },
        {
            "input": ["1+2=2"],
            "answer": "2",
            "explanation": "entering number rewrites previous result",
        },
        {
            "input": ["=5=10=15"],
            "answer": "15",
        },
    ],
    "Extra": [
        {
            "input": ["000005+003"],
            "answer": "3",
        },
        {
            "input": ["000005+003="],
            "answer": "8",
        },
        {
            "input": ["-5-10+15"],
            "answer": "15",
        },
        {
            "input": ["-5-10+15-"],
            "answer": "0",
        },
        {
            "input": ["+1+2+3+4="],
            "answer": "10",
        },
        {
            "input": ["+"],
            "answer": "0",
        },
    ]
}
