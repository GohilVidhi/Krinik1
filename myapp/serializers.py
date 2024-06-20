from rest_framework import serializers
from .models import*




#-------------League_serializers view----------------

class League_serializers(serializers.Serializer):
    # id=serializers.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    id = serializers.IntegerField(required=False)
    league_name=serializers.CharField(max_length=20,required=True)
    short_league_name=serializers.CharField(max_length=20,required=True)
    start_league_date=serializers.CharField(max_length=20,required=True)
    end_league_date=serializers.CharField(max_length=20,required=True)
    league_image=serializers.ImageField(required=True)

    class Meta:
        models=League
        fields ='__all__'
        exclude = ('id',) 

    def create(self, validated_data):
        return League.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.league_name=validated_data.get('league_name',instance.league_name)
        
        instance.short_league_name=validated_data.get('short_league_name',instance.short_league_name)
        
        instance.start_league_date=validated_data.get('start_league_date',instance.start_league_date)
        instance.end_league_date=validated_data.get('end_league_date',instance.end_league_date)
        
        instance.league_image=validated_data.get('league_image',instance.league_image)

        instance.save()
        return instance        
    





   
#-------------Team_serializers view----------------
    

    
class Team_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    league_name = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=True)
    team_name = serializers.CharField(max_length=100, required=True)
    team_short_name=serializers.CharField(max_length=20,required=True)
    team_image=serializers.ImageField(required=True)
    team_date=serializers.DateField(read_only=True,required=False)
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ('id',) 

    

    def create(self, validated_data):
        return Team.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.league_name=validated_data.get('league_name',instance.league_name)
        instance.team_name=validated_data.get('team_name',instance.team_name)
        instance.team_short_name=validated_data.get('team_short_name',instance.team_short_name)
        instance.team_image=validated_data.get('team_image',instance.team_image)
        instance.team_date=validated_data.get('team_date',instance.team_date)

        instance.save()
        return instance 



#-------------Player_serializers view----------------

class Player_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    league_name = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=True)
    team_name = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=True)
    player_name = serializers.CharField(max_length=100, required=True)
    player_short_name=serializers.CharField(max_length=20,required=True)
    player_image=serializers.ImageField(required=True)
    total_run=serializers.IntegerField(required=False)
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ('id',) 

    

    def create(self, validated_data):
        return Player.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.league_name=validated_data.get('league_name',instance.league_name)
        instance.team_name=validated_data.get('team_name',instance.team_name)
        instance.player_name=validated_data.get('player_name',instance.player_name)
        instance.player_short_name=validated_data.get('player_short_name',instance.player_short_name)
        instance.player_image=validated_data.get('player_image',instance.player_image)
        instance.total_run=validated_data.get('total_run',instance.total_run)
 
        instance.save()
        return instance
