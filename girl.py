{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPynOD1H48qHVfU8Z6XIDoS"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 393
        },
        "id": "MbvHVdV11Drv",
        "outputId": "7a2ec298-227e-4221-db8a-33018f17010b"
      },
      "source": [
        "import pygame\n",
        "import sys\n",
        "\n",
        "pygame.init()\n",
        "size = (800,600)\n",
        "image = \"../res/walking_animation.png\"\n",
        "screen = pygame.display.set_mode(size)\n",
        "x = 400\n",
        "y = 200\n",
        "speed_x = 3\n",
        "speed_y = 3\n",
        "clock = pygame.time.Clock()\n",
        "\n",
        "\n",
        "while True:\n",
        "  for event in pygame.event.get():\n",
        "    if event.type == QUIT():\n",
        "      sys.exit()\n",
        "    if (x > 800 or x < 0):\n",
        "      speed_x*=-1\n",
        "      \n",
        "\n",
        "    x+=speed_x\n",
        "\n",
        "\n",
        "screen.fill(255,0,255)\n",
        "pygame.draw.rect(screen, image, (x,y,80,80))\n",
        "\n",
        "pygame.display.flip()\n",
        "clock.tick(60)\n",
        "\n",
        "\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-d211001d7325>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mpygame\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mpygame\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0msize\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m800\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m600\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pygame'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ]
        }
      ]
    }
  ]
}