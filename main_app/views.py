from django.shortcuts import render

finches = [
    {'name': 'Black Rosy-Finch', 'populationTrend': 'Decreasing', 'note': 'The Black Rosy-Finches nest in secluded crevasses along cliffs in alpine areas.'},
    {'name': 'Common Redpoll', 'populationTrend': 'Unknown', 'note': 'Common Redpolls sometimes escape the cold of winter nights by burrowing into snow. (To keep redpolls and other birds safe at feeders, it is recommended that you clean your feeders with a diluted bleach solution several times a week, and make sure feeders are dry before filling them with seed. This helps prevent salmonella and other infections.)'},
    {'name': 'Cassia Crossbill', 'populationTrend': 'Decreasing', 'note': 'The Cassia Crossbill was once considered to be one of ten types of Red Crossbill. However, by 2017, careful study revealed that it doesn\'t migrate or breed with other crossbills. Its name comes from Cassia County, Idaho.'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })