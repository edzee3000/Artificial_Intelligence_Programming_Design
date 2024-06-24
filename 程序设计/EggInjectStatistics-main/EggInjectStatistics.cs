using System.Collections;
using System.Collections.Generic;
using System.Text;
using UnityEditor;
using UnityEngine;
using Random = System.Random;

public static class EggInjectStatistics
{
    [MenuItem("Tools/计算掼蛋概率")]
    public static void CalStatistics()
    {
        int calTimes = 1000000;
        var deck = GeneDeck();
        var random = new Random();
        List<List<int>> allStats = new List<List<int>>();
        List<long> allStatsTotal = new List<long>();
        for (int i = 0; i < calTimes; i++)
        {
            var allPlayers = DealCards(deck, random);
            foreach (var player in allPlayers)
            {
                var cards = ArrangeCards(player);
                var results = AnalysisCards(cards);
                allStats.Add(results);
                if (allStatsTotal.Count == 0)
                {
                    foreach (var result in results)
                    {
                        allStatsTotal.Add(result);
                    }
                }
                else
                {
                    for (int j = 0; j < results.Count; j++)
                    {
                        allStatsTotal[j] += results[j];
                    }
                }
            }
        }
        
        List<string> propNames = new List<string>
        {
            "天王炸",
            "炸弹总数量",
            "同花顺",
            "细分 - 皇家同花顺",
            
            "炸弹8",
            "炸弹7",
            "炸弹6",
            "炸弹5",
            "炸弹4",

            "顺子",
            "三连对",
            "飞机",
            
            "王的数量",
            "大王数量",
            "小王数量",
            "三张",
            "对子",
            "单张",
            
            "不剔除的顺子",
            "不剔除的三连对",
            "不剔除的飞机",
            "套牌之前的3张",
            "套牌之前的对子",
            "套牌之前的单张",
            "套牌之前的断牌",
            "被重复使用的卡数",
            "被重复使用的次数",
        };

        //结果写入csv，做图标统计
        StringBuilder csvBuilder = new StringBuilder();
        csvBuilder.Append("ID,");
        for (int i = 0; i < propNames.Count; i++)
        {
            csvBuilder.Append($"{propNames[i]},");
        }
        
        for (int j = 0; j < allStats.Count; j++)
        {
            csvBuilder.AppendLine();
            var singleStats = allStats[j];
            csvBuilder.Append($"{j},");
            for (int i = 0; i < singleStats.Count; i++)
            {
                csvBuilder.Append($"{singleStats[i]},");
            }
        }
        // Debug.Log(csvBuilder);
        
        string csvPath = $"{Application.dataPath}/pokerStats.csv";
        System.IO.File.WriteAllText(csvPath, csvBuilder.ToString());
        
        StringBuilder sb = new();
        for (int i = 0; i < allStatsTotal.Count; i++)
        {
            var totalStats = allStatsTotal[i];
            sb.AppendLine($"{propNames[i]}：{totalStats / (float)calTimes / 4}");
        }
        Debug.Log(sb);
    }

    private static List<Card> GeneDeck()
    {
        List<Card> deck = new List<Card>();
        for (int i = 0; i < 14; i++)
        {
            for (int k = 0; k < 2; k++)
            {
                if (k == 1 && i == 0)
                {
                    continue;
                }

                for (int j = 0; j < 4; j++)
                {
                    deck.Add(new Card(i, (CardType)j));
                }
            }
        }

        Debug.Log($"牌数：{deck.Count}");
        return deck;
    }

    private static List<List<Card>> DealCards(List<Card> deck, Random random)
    {
        List<List<Card>> allPlayers = new List<List<Card>>();
        for (int i = 0; i < 4; i++)
        {
            allPlayers.Add(new List<Card>());
        }

        var n = deck.Count;
        while (n > 1)
        {
            n--;
            var k = random.Next(0, n + 1);
            (deck[k], deck[n]) = (deck[n], deck[k]);
        }

        for (int i = 0; i < 27; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                var card = deck[i * 4 + j];
                allPlayers[j].Add(card);
            }
        }

        return allPlayers;
    }

    private static bool[][] ArrangeCards(List<Card> player)
    {
        bool[][] cardArray = new bool[14][];
        for (int i = 0; i < cardArray.Length; i++)
        {
            cardArray[i] = new bool[8];
            for (int j = 0; j < 8; j++)
            {
                cardArray[i][j] = false;
            }
        }

        // StringBuilder debug = new();
        // player.Sort((t1,t2) =>t1.number.CompareTo(t2.number));
        // debug.Append("牌：");
        foreach (var card in player)
        {
            if (cardArray[card.number][(int)card.type])
            {
                cardArray[card.number][4 + (int)card.type] = true;
            }
            else
            {
                cardArray[card.number][(int)card.type] = true;
            }

            // debug.Append($"[{card.number}:{(int)card.type}]");
        }
        
        // debug.AppendLine("计数:");
        // for (int i = 0; i < cardArray.Length; i++)
        // {
        //     int numCount = 0;
        //     for (int j = 0; j < 8; j++)
        //     {
        //         if (cardArray[i][j])
        //         {
        //             numCount++;
        //         }
        //     }
        //     debug.Append($"[{i}:{numCount}]");
        // }
        // Debug.Log(debug);
        return cardArray;
    }

    private static List<int> AnalysisCards(bool[][] card)
    {
        int totalBombs = 0;
        //大小王
        int numOfJokers = 0;
        int numOfBigJokers = 0;
        int numOfSmallJokers = 0;
        for (int i = 0; i < 4; i++)
        {
            if (card[0][i])
            {
                numOfJokers++;
                if (i < 2)
                {
                    numOfBigJokers++;
                }
                else
                {
                    numOfSmallJokers++;
                }
            }

            card[0][i] = false;
        }

        int numOfStraightFlush = 0;
        List<int> startOfStraightsFlush = new List<int>();

        //皇家同花顺
        int numOfRoyleFlush = 0;
        for (int k = 0; k < 8; k++)
        {
            bool isRoyleFlush = true;
            for (int j = 0; j < 4; j++)
            {
                if (!card[10 + j][k])
                {
                    isRoyleFlush = false;
                }
            }

            if (!card[1][k])
            {
                isRoyleFlush = false;
            }

            if (isRoyleFlush)
            {
                numOfStraightFlush++;
                numOfRoyleFlush++;
                totalBombs++;
                startOfStraightsFlush.Add(10);

                for (int j = 0; j < 4; j++)
                {
                    card[10 + j][k] = false;
                }

                card[1][k] = false;
            }
        }

        //同花顺
        for (int i = 1; i < 10; i++)
        {
            if (i < card.Length - 5)
            {
                for (int k = 0; k < 8; k++)
                {
                    bool isStraightFlush = true;
                    for (int j = 0; j < 5; j++)
                    {
                        if (!card[i + j][k])
                        {
                            isStraightFlush = false;
                        }
                    }

                    if (isStraightFlush)
                    {
                        numOfStraightFlush++;
                        totalBombs++;
                        startOfStraightsFlush.Add(i);
                        for (int j = 0; j < 5; j++)
                        {
                            card[i + j][k] = false;
                        }
                    }
                }
            }
        }

        //炸弹
        List<int> numOf8 = new List<int>();
        List<int> numOf7 = new List<int>();
        List<int> numOf6 = new List<int>();
        List<int> numOf5 = new List<int>();
        List<int> numOf4 = new List<int>();

        int preNumOf3 = 0;
        int preNumOf2 = 0;
        int preNumOf1 = 0;
        int breakNum = 0;
        int[] cardCounts = new int[card.Length];
        for (int i = 1; i < card.Length; i++)
        {
            int numCount = 0;
            for (int j = 0; j < 8; j++)
            {
                if (card[i][j])
                {
                    numCount++;
                }
            }

            cardCounts[i - 1] = numCount;
            if (i == 1)
            {
                cardCounts[card.Length - 1] = numCount;
            }

            switch (numCount)
            {
                case 8:
                    numOf8.Add(i - 1);
                    totalBombs += 2;
                    break;
                case 7:
                    numOf7.Add(i - 1);
                    totalBombs++;
                    break;
                case 6:
                    numOf6.Add(i - 1);
                    totalBombs++;
                    break;
                case 5:
                    numOf5.Add(i - 1);
                    totalBombs++;
                    break;
                case 4:
                    numOf4.Add(i - 1);
                    totalBombs++;
                    break;
                case 3:
                    preNumOf3++;
                    break;
                case 2:
                    preNumOf2++;
                    break;
                case 1:
                    preNumOf1++;
                    break;
                case 0:
                    breakNum++;
                    break;
            }
        }

        List<int> copyCardCounts = new List<int>(cardCounts);

        //顺子、三联对、飞机计算器
        int numOfStraights = 0;
        List<int> startOfStraights = new List<int>();
        int numOf3Pairs = 0;
        List<int> startOf3Pairs = new List<int>();
        int numOfAirplane = 0;
        List<int> startOfAirplanes = new List<int>();
        for (int i = 0; i < cardCounts.Length; i++)
        {
            //飞机
            if (i < cardCounts.Length - 2)
            {
                bool isAirPlane = true;
                for (int j = 0; j < 2; j++)
                {
                    if (cardCounts[i + j] <= 2)
                    {
                        isAirPlane = false;
                    }
                }

                if (isAirPlane)
                {
                    numOfAirplane++;
                    startOfAirplanes.Add(i);
                }
            }

            //三联对
            if (i < cardCounts.Length - 3)
            {
                bool is3Pairs = true;
                for (int j = 0; j < 3; j++)
                {
                    if (cardCounts[i + j] <= 1)
                    {
                        is3Pairs = false;
                    }
                }

                if (is3Pairs)
                {
                    numOf3Pairs++;
                    startOf3Pairs.Add(i);
                }
            }

            //顺子
            if (i < cardCounts.Length - 5)
            {
                bool isStraight = true;
                for (int j = 0; j < 5; j++)
                {
                    if (cardCounts[i + j] <= 0)
                    {
                        isStraight = false;
                    }
                }

                if (isStraight)
                {
                    numOfStraights++;
                    startOfStraights.Add(i);
                }
            }
        }

        int repeatedCards = 0;
        int repeatedTimes = 0;

        //剔除
        for (int i = 0; i < startOfAirplanes.Count; i++)
        {
            for (int j = 0; j < 2; j++)
            {
                if (i + j == cardCounts.Length - 1)
                {
                    cardCounts[0] -= 3;
                    if (cardCounts[0] < 0)
                    {
                        repeatedTimes++;
                        repeatedCards += cardCounts[0];
                    }
                }
                else
                {
                    cardCounts[i + j] -= 3;
                    if (cardCounts[i + j] < 0)
                    {
                        repeatedTimes++;
                        repeatedCards += cardCounts[0];
                    }
                }
            }
        }

        for (int i = 0; i < startOf3Pairs.Count; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (i + j == cardCounts.Length - 1)
                {
                    cardCounts[0] -= 2;
                    if (cardCounts[0] < 0)
                    {
                        repeatedTimes++;
                        repeatedCards += cardCounts[0];
                    }
                }
                else
                {
                    cardCounts[i + j] -= 2;
                    if (cardCounts[i + j] < 0)
                    {
                        repeatedTimes++;
                        repeatedCards += cardCounts[i + j];
                    }
                }
            }
        }

        for (int i = 0; i < startOfStraights.Count; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (i + j == cardCounts.Length - 1)
                {
                    cardCounts[0] -= 1;
                    if (cardCounts[0] < 0)
                    {
                        repeatedTimes++;
                        repeatedCards += cardCounts[0];
                    }
                }
                else
                {
                    cardCounts[i + j] -= 1;
                    if (cardCounts[i + j] < 0)
                    {
                        repeatedTimes++;
                        repeatedCards += cardCounts[i + j];
                    }
                }
            }
        }

        for (int i = 0; i < numOf8.Count; i++)
        {
            int index = numOf8[i];
            cardCounts[index] -= 8;
            copyCardCounts[index] -= 8;
            if (cardCounts[index] < 0)
            {
                repeatedTimes++;
                repeatedCards += cardCounts[index];
            }
        }

        for (int i = 0; i < numOf7.Count; i++)
        {
            int index = numOf7[i];
            cardCounts[index] -= 7;
            copyCardCounts[index] -= 7;
            if (cardCounts[index] < 0)
            {
                repeatedTimes++;
                repeatedCards += cardCounts[index];
            }
        }

        for (int i = 0; i < numOf6.Count; i++)
        {
            int index = numOf6[i];
            cardCounts[index] -= 6;
            copyCardCounts[index] -= 6;
            if (cardCounts[index] < 0)
            {
                repeatedTimes++;
                repeatedCards += cardCounts[index];
            }
        }

        for (int i = 0; i < numOf5.Count; i++)
        {
            int index = numOf5[i];
            cardCounts[index] -= 5;
            copyCardCounts[index] -= 5;
            if (cardCounts[index] < 0)
            {
                repeatedTimes++;
                repeatedCards += cardCounts[index];
            }
        }

        for (int i = 0; i < numOf4.Count; i++)
        {
            int index = numOf4[i];
            cardCounts[index] -= 4;
            copyCardCounts[index] -= 4;
            if (cardCounts[index] < 0)
            {
                repeatedTimes++;
                repeatedCards += cardCounts[index];
            }
        }

        int numOfStraights_none = 0;
        int numOf3Pairs_none = 0;
        int numOfAirplane_none = 0;
        for (int i = 0; i < copyCardCounts.Count - 2; i++)
        {
            //飞机
            bool isAirPlane = true;
            for (int j = 0; j < 2; j++)
            {
                if (copyCardCounts[i + j] <= 2)
                {
                    isAirPlane = false;
                }
            }

            if (isAirPlane)
            {
                numOfAirplane_none++;
                for (int j = 0; j < 2; j++)
                {
                    copyCardCounts[i + j] -= 3;
                    if (i + j == copyCardCounts.Count - 1)
                    {
                        copyCardCounts[0] -= 3;
                    }
                    else if (i + j == 0)
                    {
                        copyCardCounts[^1] -= 3;
                    }
                }
            }
        }

        for (int i = 0; i < copyCardCounts.Count - 3; i++)
        {
            //三联对
            bool is3Pairs = true;
            for (int j = 0; j < 3; j++)
            {
                if (copyCardCounts[i + j] <= 1)
                {
                    is3Pairs = false;
                }
            }

            if (is3Pairs)
            {
                numOf3Pairs_none++;
                for (int j = 0; j < 3; j++)
                {
                    copyCardCounts[i + j] -= 2;
                    if (i + j == copyCardCounts.Count - 1)
                    {
                        copyCardCounts[0] -= 2;
                    }
                    else if (i + j == 0)
                    {
                        copyCardCounts[^1] -= 2;
                    }
                }
            }
        }

        for (int i = 0; i < copyCardCounts.Count - 5; i++)
        {
            //顺子
            bool isStraight = true;
            for (int j = 0; j < 5; j++)
            {
                if (copyCardCounts[i + j] <= 0)
                {
                    isStraight = false;
                }
            }

            if (isStraight)
            {
                numOfStraights_none++;
                for (int j = 0; j < 5; j++)
                {
                    copyCardCounts[i + j] -= 1;
                    if (i + j == copyCardCounts.Count - 1)
                    {
                        copyCardCounts[0] -= 1;
                    }
                    else if (i + j == 0)
                    {
                        copyCardCounts[^1] -= 1;
                    }
                }
            }
        }

        int numOf3 = 0;
        int numOf2 = 0;
        int numOf1 = 0;

        for (int i = 0; i < copyCardCounts.Count - 1; i++)
        {
            var cardCount = copyCardCounts[i];
            switch (cardCount)
            {
                case 3:
                    numOf3++;
                    break;
                case 2:
                    numOf2++;
                    break;
                case 1:
                    numOf1++;
                    break;
            }
        }

        if (numOfJokers >= 4)
        {
            totalBombs++;
        }

        List<int> analysis = new List<int>();
        //炸弹
        analysis.Add(numOfJokers >= 4? 1 : 0); //"天王炸"
        analysis.Add(totalBombs); //炸弹总数量
        analysis.Add(numOfStraightFlush); //"同花顺"
        analysis.Add(numOfRoyleFlush); //细分 - 皇家同花顺

        analysis.Add(numOf8.Count); //炸弹8
        analysis.Add(numOf7.Count); //炸弹7
        analysis.Add(numOf6.Count); //炸弹6
        analysis.Add(numOf5.Count); //炸弹5
        analysis.Add(numOf4.Count); //炸弹4

        //大套牌
        
        analysis.Add(numOfStraights_none); //顺子
        analysis.Add(numOf3Pairs_none); //三连对
        analysis.Add(numOfAirplane_none); //飞机

        //小套牌
        analysis.Add(numOfJokers); //"王的数量"
        analysis.Add(numOfBigJokers); //"大王数量"
        analysis.Add(numOfSmallJokers); //"小王数量"
        analysis.Add(numOf3); //三张
        analysis.Add(numOf2); //对子
        analysis.Add(numOf1); //单张

        //分析
        analysis.Add(numOfStraights); //不剔除的顺子
        analysis.Add(numOf3Pairs); //不剔除的三连对
        analysis.Add(numOfAirplane); //不剔除的飞机
        analysis.Add(preNumOf3); //套牌之前的3张
        analysis.Add(preNumOf2); //套牌之前的对子
        analysis.Add(preNumOf1); //套牌之前的单张
        analysis.Add(breakNum); //套牌之前的断牌
        analysis.Add(repeatedCards); //被重复使用的卡数
        analysis.Add(repeatedTimes); //被重复使用的次数

        return analysis;
    }
}

public class Card
{
    public Card(int num, CardType type)
    {
        this.number = num;
        this.type = type;
    }

    public CardType type;
    public int number; // 0 is joker
}

public enum CardType
{
    Heart,
    Diamond,
    Spade,
    Club
}