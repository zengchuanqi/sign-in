import pytest

name = 'zengchuantu'
age = 18
print('my name is %s,age is %d' % (name,age))
print(f'my name is {name},age is {age}')
print('my name is {},age is {}'.format(name,age))


data_1 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        'user': 3,
        'pwd': 4
    }
)


@pytest.mark.parametrize('dic', data_1)
def test_parametrize_1(dic):
    print(f':{dic["user"]},{dic["pwd"]}')