from googlesearch import search
from bs4 import BeautifulSoup
import requests
Menus = [ '''<!-- component -->
<div class="h-16 w-full bg-black bg-opacity-50">
        <div class="w-full h-full flex justify-center items-center">
            <div
                class="flex h-full items-center  hover:bg-black hover:bg-opacity-50">
                <div class="mx-4 text-white">Opcion</div>
                <div class=" h-8 w-px bg-gray-300"></div>
            </div>
            <div class="flex h-full items-center  hover:bg-black hover:bg-opacity-50">
                <div class="mx-4 text-white">Opcion</div>
                <div class=" h-8 w-px bg-gray-300"></div>
            </div>
            <div class="flex h-full items-center  hover:bg-black hover:bg-opacity-50">
                <div class="mx-4 text-white">Opcion</div>
                <div class=" h-8 w-px bg-gray-300"></div>
            </div>
            <div class="flex h-full items-center  hover:bg-black hover:bg-opacity-50">
                <div class="mx-4 text-white">Opcion</div>
                <div class=" h-8 w-px bg-gray-300"></div>
            </div>
            <div class="flex h-full  items-center hover:bg-black hover:bg-opacity-50">
                <div class="mx-4 text-white">Opcion</div>
            </div>
        </div>
    </div>''', '''<!-- component -->
<!-- Header -->
<header>
  <!-- navbar and menu -->
  <nav class="shadow">

  <div class="flex justify-between items-center py-6 px-10 container mx-auto">

    <div>
      <h1 class="text-2xl font-bold bg-gradient-to-tr from-indigo-600 to-green-600 bg-clip-text text-transparent hover:cursor-pointer">Adsla</h1>
    </div>

    <div>
      
      <div class="hover:cursor-pointer sm:hidden">
        <spnan class="h-1 rounded-full block w-8 mb-1 bg-gradient-to-tr from-indigo-600 to-green-600"></spnan>
        <spnan class="h-1 rounded-full block w-8 mb-1 bg-gradient-to-tr from-indigo-600 to-green-600"></spnan>
        <spnan class="h-1 rounded-full block w-8 mb-1 bg-gradient-to-tr from-indigo-600 to-green-600"></spnan>
      </div>
      <div class="flex items-center">

        <ul class="sm:flex space-x-4 hidden items-center">
          <li><a href="#" class="text-gray-700 hover:text-indigo-600 text-md ">Home</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600 text-md ">About</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600 text-md ">Services</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600 text-md ">Products</a></li>
          <li><a href="#" class="text-gray-700 hover:text-indigo-600 text-md ">Contact</a></li>
        </ul>

        <div class="md:flex items-center hidden space-x-4 ml-8 lg:ml-12">
          <h1 class="text-text-gray-600  py-2 hover:cursor-pointer hover:text-indigo-600">LOGIN</h1>
          <h1 class="text-text-gray-600  py-2 hover:cursor-pointer px-4 rounded text-white bg-gradient-to-tr from-indigo-600 to-green-600 hover:shadow-lg">SIGNUP</h1>
        </div>
      </div>
    </div>
  </div>
  </nav>
</header>
<main>
  <!-- section hero -->
  <section>
    <div class="bg-gray-100 sm:grid grid-cols-5 grid-rows-2 px-4 py-6 min-h-full lg:min-h-screen space-y-6 sm:space-y-0 sm:gap-4">

    <div class="h-96 col-span-4 bg-gradient-to-tr from-indigo-800 to-indigo-500 rounded-md flex items-center">
      <div class="ml-20 w-80">
      <h2 class="text-white text-4xl">Adsla</h2>
      <p class="text-indigo-100 mt-4 capitalize font-thin tracking-wider leading-7">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed, dolore?</p>

      <a href="#" class="uppercase inline-block mt-8 text-sm bg-white py-2 px-4 rounded font-semibold hover:bg-indigo-100">get start</a>
      </div>

    </div>
    <div class="h-96 col-span-1 ">
      <div class="bg-white py-3 px-4 rounded-lg flex justify-around items-center ">
   <input type="text" placeholder="seach" class=" bg-gray-100 rounded-md  outline-none pl-2 ring-indigo-700 w-full mr-2 p-2">
  <span><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor ">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
</svg></span>
      </div>
      <div class="bg-white  rounded-md">

      <h1 class="text-center text-xl my-4  bg-white py-2 rounded-md border-b-2 cursor-pointer  text-gray-600">Service</h1>
      <div class="bg-white rounded-md list-none  text-center ">
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Products</a></li>
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Models</a></li>
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Pricing</a></li>
        <li class="py-3 border-b-2"><a href="#" class="list-none  hover:text-indigo-600">Hire</a></li>
        <li class="py-3 "><a href="#" class="list-none border-b-2 hover:text-indigo-600">Business</a></li>
      </div>
      </div>
    </div>
    </div>

  </section>

</main>''', '''<!-- component -->
<div class="w-full">
    <nav class="bg-white shadow-lg">
        <div class="md:flex items-center justify-between py-2 px-8 md:px-12">
            <div class="flex justify-between items-center">
               <div class="text-2xl font-bold text-gray-800 md:text-3xl">
                    <a href="#">Brand</a>
               </div>
                <div class="md:hidden">
                    <button type="button" class="block text-gray-800 hover:text-gray-700 focus:text-gray-700 focus:outline-none">
                        <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
                            <path class="hidden" d="M16.24 14.83a1 1 0 0 1-1.41 1.41L12 13.41l-2.83 2.83a1 1 0 0 1-1.41-1.41L10.59 12 7.76 9.17a1 1 0 0 1 1.41-1.41L12 10.59l2.83-2.83a1 1 0 0 1 1.41 1.41L13.41 12l2.83 2.83z"/>
                            <path d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"/>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="flex flex-col md:flex-row hidden md:block -mx-2">
                <a href="#" class="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2">Home</a>
                <a href="#" class="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2">About</a>
                <a href="#" class="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2">Contact</a>
            </div>
        </div>
    </nav>
    <div class="flex bg-white" style="height:600px;">
        <div class="flex items-center text-center lg:text-left px-8 md:px-12 lg:w-1/2">
            <div>
                <h2 class="text-3xl font-semibold text-gray-800 md:text-4xl">Build Your New <span class="text-indigo-600">Idea</span></h2>
                <p class="mt-2 text-sm text-gray-500 md:text-base">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis commodi cum cupiditate ducimus, fugit harum id necessitatibus odio quam quasi, quibusdam rem tempora voluptates. Cumque debitis dignissimos id quam vel!</p>
                <div class="flex justify-center lg:justify-start mt-6">
                    <a class="px-4 py-3 bg-gray-900 text-gray-200 text-xs font-semibold rounded hover:bg-gray-800" href="#">Get Started</a>
                    <a class="mx-4 px-4 py-3 bg-gray-300 text-gray-900 text-xs font-semibold rounded hover:bg-gray-400" href="#">Learn More</a>
                </div>
            </div>
        </div>
        <div class="hidden lg:block lg:w-1/2" style="clip-path:polygon(10% 0, 100% 0%, 100% 100%, 0 100%)">
            <div class="h-full object-cover" style="background-image: url(https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1352&q=80)">
                <div class="h-full bg-black opacity-25"></div>
            </div>
        </div>
    </div>
</div>''', '''<!-- component -->
<div
                                            class="h-full flex flex-col bg-gray-100 dark:bg-gray-700 shadow-xl overflow-y-scroll">
                                            <div class="ml-3 h-7 flex justify-end items-center">
                                                <button type="button"
                                                    class="bg-gray-100 dark:bg-gray-700 m-1 p-3 justify-end rounded-md text-gray-400 hover:text-gray-500 focus:ring-2 focus:ring-indigo-500">
                                                    <span class="sr-only">Close panel</span>
                                                    <!-- Heroicon name: outline/x -->
                                                    <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg"
                                                        fill="none" viewBox="0 0 24 24" stroke="currentColor"
                                                        aria-hidden="true">
                                                        <path stroke-linecap="round" stroke-linejoin="round"
                                                            stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                                    </svg>
                                                </button>
                                            </div>
                                            <div class="bg-green-300 shadow-lg pb-3 rounded-b-3xl">
                                                <div
                                                    class="flex  rounded-b-3xl bg-gray-100 dark:bg-gray-700 space-y-5 flex-col items-center py-7">
                                                    <img class="h-28 w-28 rounded-full"
                                                        src="https://api.lorem.space/image/face?w=120&h=120&hash=bart89fe"
                                                        alt="User">
                                                    <a href="#"> <span
                                                            class="text-h1">Michele</span></a>
                                                </div>
                                                <div
                                                    class="grid px-7 py-2  items-center justify-around grid-cols-3 gap-4 divide-x divide-solid ">
                                                    <div class="col-span-1 flex flex-col items-center ">
                                                        <span class="text-2xl font-bold dark:text-gray-500">4</span>
                                                        <span class="text-lg font-medium 0">Ranking</span>
                                                    </div>
                                                    <div class="col-span-1 px-3 flex flex-col items-center ">
                                                        <span class="text-2xl font-bold dark:text-gray-500">
                                                           Free</span>
                                                        <span class="text-lg font-medium">Plan</span>
                                                    </div>
                                                    <div class="col-span-1 px-3 flex flex-col items-center ">
                                                        <span class="text-2xl font-bold dark:text-gray-500">
                                                            546</span>
                                                        <span class="text-lg font-medium">Puntos</span>
                                                    </div>
                                                </div>

                                            </div>

                                            <div
                                                class="grid rounded-2xl divide-y divide-dashed hover:divide-solid  justify-evenly bg-gray-50 dark:bg-gray-300 m-3 mt-10 grid-cols-3">
                                                <div class="col-span-1  p-3">
                                                    <div class="flex flex-col items-center ">
                                                        <a href=""> <button
                                                                class="tr-300">
                                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                                    class="h-14 w-14 text-gray-500" fill="none"
                                                                    viewBox="0 0 24 24" stroke="currentColor"
                                                                    stroke-width="2">
                                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                                        d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                                                </svg>
                                                                <span class="text-lg font-medium">Mi Perfil</span>
                                                            </button></a>
                                                    </div>
                                                </div>
                                                <div class="col-span-1  p-3">
                                                    <div class="flex flex-col items-center ">
                                                        <a href=""> <button
                                                                class="tr-300">
                                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                                    class="h-14 w-14 text-gray-500" fill="none"
                                                                    viewBox="0 0 24 24" stroke="currentColor"
                                                                    stroke-width="2">
                                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                                        d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
                                                                </svg>
                                                                <span class="text-lg font-medium">Mis dinero</span>
                                                            </button></a>
                                                    </div>
                                                </div>
                                                <div class="col-span-1  p-3">
                                                    <div class="flex flex-col items-center ">
                                                        <a href=""> <button
                                                                class="tr-300">
                                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                                    class="h-14 w-14 text-gray-500" fill="none"
                                                                    viewBox="0 0 24 24" stroke="currentColor"
                                                                    stroke-width="2">
                                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                                        d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z" />
                                                                </svg>
                                                                <span class="text-lg font-medium">Mis referidos</span>
                                                            </button></a>
                                                    </div>
                                                </div>
                                                <div class="col-span-1  p-3">
                                                    <div class="flex flex-col items-center ">
                                                        <a href="">
                                                            <button class="tr-300">
                                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                                    class="h-14 w-14 text-gray-500" fill="none"
                                                                    viewBox="0 0 24 24" stroke="currentColor"
                                                                    stroke-width="2">
                                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                                        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                                                </svg>
                                                                <span class="text-lg font-medium">Mis facturas</span>
                                                            </button></a>
                                                    </div>
                                                </div>
                                                <div class="col-span-1  p-3">
                                                    <div class="flex flex-col items-center ">
                                                        <a href=""> <button class="tr-300">
                                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                                    class="h-14 w-14 text-gray-500" fill="none"
                                                                    viewBox="0 0 24 24" stroke="currentColor"
                                                                    stroke-width="2">
                                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                                        d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                                                </svg>
                                                                <span class="text-lg font-medium">Ayuda</span>
                                                            </button></a>
                                                    </div>
                                                </div>
                                                <div class="col-span-1 bg-red-50 p-3">
                                                    <div class="flex  flex-col items-center ">
                                                        <a href=""> <button class="tr-300">
                                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                                    class="h-14 w-14 text-gray-500" fill="none"
                                                                    viewBox="0 0 24 24" stroke="currentColor"
                                                                    stroke-width="2">
                                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                                        d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                                                                </svg>
                                                                <span class="text-lg font-medium">Salir</span>
                                                            </button></a>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="flex mx-auto mt-3 w-100 ">
                                                <a href=""> <button
                                                        class="p-2 shadow-lg rounded-2xl tr-300 w-100 font-medium  bg-green-500 rounded-md hover:bg-green-600 text-gray-50">Mejorar
                                                        membresía</button></a>
                                            </div>
                                        </div>''', '''<!-- component -->
<!-- This is an example component -->
<div class='relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12'>
  <div class="flex items-center justify-between border-b bg-blue-400 p-3">
    <div class="flex items-center space-x-2 rounded bg-gray-100 py-1 px-2 text-slate-500 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-4 w-4">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75" />
      </svg>
      <span>Back</span>
    </div>
    <div class="text-lg font-bold text-gray-100">filename.pdf</div>
    <div class="flex items-center space-x-5 text-gray-100">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
        <path fill-rule="evenodd" d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z" clip-rule="evenodd" />
      </svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
        <path fill-rule="evenodd" d="M5.625 1.5H9a3.75 3.75 0 013.75 3.75v1.875c0 1.036.84 1.875 1.875 1.875H16.5a3.75 3.75 0 013.75 3.75v7.875c0 1.035-.84 1.875-1.875 1.875H5.625a1.875 1.875 0 01-1.875-1.875V3.375c0-1.036.84-1.875 1.875-1.875zm6.905 9.97a.75.75 0 00-1.06 0l-3 3a.75.75 0 101.06 1.06l1.72-1.72V18a.75.75 0 001.5 0v-4.19l1.72 1.72a.75.75 0 101.06-1.06l-3-3z" clip-rule="evenodd" />
        <path d="M14.25 5.25a5.23 5.23 0 00-1.279-3.434 9.768 9.768 0 016.963 6.963A5.23 5.23 0 0016.5 7.5h-1.875a.375.375 0 01-.375-.375V5.25z" />
      </svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
        <path fill-rule="evenodd" d="M5.625 1.5H9a3.75 3.75 0 013.75 3.75v1.875c0 1.036.84 1.875 1.875 1.875H16.5a3.75 3.75 0 013.75 3.75v7.875c0 1.035-.84 1.875-1.875 1.875H5.625a1.875 1.875 0 01-1.875-1.875V3.375c0-1.036.84-1.875 1.875-1.875zm5.845 17.03a.75.75 0 001.06 0l3-3a.75.75 0 10-1.06-1.06l-1.72 1.72V12a.75.75 0 00-1.5 0v4.19l-1.72-1.72a.75.75 0 00-1.06 1.06l3 3z" clip-rule="evenodd" />
        <path d="M14.25 5.25a5.23 5.23 0 00-1.279-3.434 9.768 9.768 0 016.963 6.963A5.23 5.23 0 0016.5 7.5h-1.875a.375.375 0 01-.375-.375V5.25z" />
      </svg>
    </div>
  </div>
</div>''', '''<!-- component -->
<div class="relative py-16 bg-gradient-to-br from-sky-50 to-gray-200">  
    <div class="relative container m-auto px-6 text-gray-500 md:px-12 xl:px-40">
        <div class="m-auto md:w-8/12 lg:w-6/12 xl:w-6/12">
            <div class="rounded-xl bg-white shadow-xl">
                <div class="p-6 sm:p-16">
                    <div class="space-y-4">
                        
                        <h2 class="mb-8 text-2xl text-cyan-900 font-bold">Landing Page Heading<br>
                        Heading Content</h2>
                    </div>
                    <div class="mt-16 grid space-y-4">
                        <button class="group h-12 px-6 border-2 border-gray-300 rounded-full transition duration-300 
 hover:border-blue-400 focus:bg-blue-50 active:bg-blue-100">
                            <div class="relative flex items-center space-x-4 justify-center">
                                <a href="">
                                <span class="block w-max font-semibold tracking-wide text-gray-700 text-sm transition duration-300 group-hover:text-blue-600 sm:text-base">Title 1</span>
                            </a>
                            </div>
                        </button>
                        <button class="group h-12 px-6 border-2 border-gray-300 rounded-full transition duration-300 
 hover:border-blue-400 focus:bg-blue-50 active:bg-blue-100">
                            <div class="relative flex items-center space-x-4 justify-center">
                                
                                <a href="">
                                <span class="block w-max font-semibold tracking-wide text-gray-700 text-sm transition duration-300 group-hover:text-blue-600 sm:text-base">Title 2</span>
                            </a></div>
                        </button>
                        <button class="group h-12 px-6 border-2 border-gray-300 rounded-full transition duration-300 
                                     hover:border-blue-400 focus:bg-blue-50 active:bg-blue-100">
                            <div class="relative flex items-center space-x-4 justify-center">
                                 
                                <a href="">
                                <span class="block w-max font-semibold tracking-wide text-gray-700 text-sm transition duration-300 group-hover:text-blue-600 sm:text-base">Title 3</span>
                            </a></div>
                        </button>
                        <button class="group h-12 px-6 border-2 border-gray-300 rounded-full transition duration-300 
                                     hover:border-blue-400 focus:bg-blue-50 active:bg-blue-100">
                            <div class="relative flex items-center space-x-4 justify-center">
                                 
                                <a href="">
                                <span class="block w-max font-semibold tracking-wide text-gray-700 text-sm transition duration-300 group-hover:text-blue-600 sm:text-base">Title 4</span>
                            </a></div>
                        </button>
                        <button class="group h-12 px-6 border-2 border-gray-300 rounded-full transition duration-300 
                                     hover:border-blue-400 focus:bg-blue-50 active:bg-blue-100">
                            <div class="relative flex items-center space-x-4 justify-center">
                                 
                                <a href="">
                                <span class="block w-max font-semibold tracking-wide text-gray-700 text-sm transition duration-300 group-hover:text-blue-600 sm:text-base">Title 5</span>
                            </a></div>
                        </button>
                    </div>

                    <div class="mt-32 space-y-4 text-gray-600 text-center sm:-mb-8">
                        <p class="text-xs">By proceeding, you agree to our <a href="" class="underline">Disclaimer</a> and confirm you have read our <a href="" class="underline">Privacy and Cookie Statement</a>.</p>
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>''']
Cards = ['''<!-- component -->
<html>
    <head>
        <link rel="stylesheet" href="https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/css/main.ad49aa9b.css" />
    </head>
    <body >
        <div class="flex flex-col justify-center items-center h-[100vh]">
            <div class="relative flex flex-col items-center rounded-[20px] w-[400px] mx-auto p-4 bg-white bg-clip-border shadow-3xl shadow-shadow-500 dark:!bg-navy-800 dark:text-white dark:!shadow-none">
                <div class="relative flex h-32 w-full justify-center rounded-xl bg-cover" >
                    <img src='https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/banner.ef572d78f29b0fee0a09.png' class="absolute flex h-32 w-full justify-center rounded-xl bg-cover"> 
                    <div class="absolute -bottom-12 flex h-[87px] w-[87px] items-center justify-center rounded-full border-[4px] border-white bg-pink-400 dark:!border-navy-700">
                        <img class="h-full w-full rounded-full" src='https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/avatar11.1060b63041fdffa5f8ef.png' alt="" />
                    </div>
                </div> 
                <div class="mt-16 flex flex-col items-center">
                    <h4 class="text-xl font-bold text-navy-700 dark:text-white">
                    Adela Parkson
                    </h4>
                    <p class="text-base font-normal text-gray-600">Product Manager</p>
                </div> 
                <div class="mt-6 mb-3 flex gap-14 md:!gap-14">
                    <div class="flex flex-col items-center justify-center">
                    <p class="text-2xl font-bold text-navy-700 dark:text-white">17</p>
                    <p class="text-sm font-normal text-gray-600">Posts</p>
                    </div>
                    <div class="flex flex-col items-center justify-center">
                    <p class="text-2xl font-bold text-navy-700 dark:text-white">
                        9.7K
                    </p>
                    <p class="text-sm font-normal text-gray-600">Followers</p>
                    </div>
                    <div class="flex flex-col items-center justify-center">
                    <p class="text-2xl font-bold text-navy-700 dark:text-white">
                        434
                    </p>
                    <p class="text-sm font-normal text-gray-600">Following</p>
                    </div>
                </div>
            </div>  
            <p class="font-normal text-navy-700 mt-20 mx-auto w-max">Profile Card component from <a href="https://horizon-ui.com?ref=tailwindcomponents.com" target="_blank" class="text-brand-500 font-bold">Horizon UI Tailwind React</a></p>  
        </div>
    </body>
</html>''', '''<!-- component -->
<!-- This is an example component -->
<div class='flex items-center justify-center min-h-screen from-[#F9F5F3] via-[#F9F5F3] to-[#F9F5F3] bg-gradient-to-br px-2'>
    <div class='w-full max-w-md  mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
        <div class='max-w-md mx-auto'>
          <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'>
           </div>
          <div class='p-4 sm:p-6'>
            <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'>Spagetti with shrimp sauce</p>
            <div class='flex flex-row'>
              <p class='text-[#3C3C4399] text-[17px] mr-2 line-through'>MVR 700</p>
              <p class='text-[17px] font-bold text-[#0FB478]'>MVR 700</p>
            </div>
            <p class='text-[#7C7C80] font-[15px] mt-6'>Our shrimp sauce is made with mozarella, a creamy taste of shrimp with extra kick of spices.</p>


              <a target='_blank' href='foodiesapp://food/1001' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
                  View on foodies
              </a>
            <a target='_blank' href="https://apps.apple.com/us/app/id1493631471" class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
                  Download app
              </a>
          </div>
        </div>
    </div>
</div>''', '''<!-- component -->
<div class="min-h-screen bg-gray-100 flex flex-col justify-center">
  <div class="relative m-3 flex flex-wrap mx-auto justify-center">
                        <div class="min-w-[340px]flex flex-col group">
                            <div
                                class="h-48 md:h-56 lg:h-[24rem] w-full bg-red-500 border-2 border-white flex items-center justify-center text-white text-base mb-3 md:mb-5 overflow-hidden relative">

                                <img src="https://pixahive.com/wp-content/uploads/2020/10/Gym-shoes-153180-pixahive.jpg"
                                    class="object-cover w-full h-full scale-100 group-hover:scale-110 transition-all duration-400"
                                    alt="">

                                <div
                                    class="absolute z-10 border-4 border-primary w-[95%] h-[95%] invisible group-hover:visible opacity-0 group-hover:opacity-100 group-hover:scale-90 transition-all duration-500">
                                </div>

                            </div>
                            <a href="./single_post.html"
                                class=" block text-black text-center hover:text-primary transition-colors duration-150 text-lg md:text-xl mb-1">
                                Wild West Hoodie</a>


                            <p class="mb-4 font-light  text-sm md:text-sm text-center text-gray-400">Lorem ipsum dolor
                                sit
                                amet, consectetur adipisicing.</p>

                            <div class="flex justify-center gap-x-3">
                                <a href="/track_order.html"
                                    class=" px-5 py-2 border border-primary text-primary hover:bg-primary  transition-all outline-none bg-black border-black text-white hover:text-black hover:bg-white font-bold">
                                    Add</a>
                                <a href="/track_order.html"
                                    class="px-5 py-2 border border-primary text-primary hover:bg-primary hover:text-white transition-all outline-none bg-white border-black text-black hover:text-white hover:bg-black font-bold">
                                    View</a>
                            </div>

                        </div>
  </div>
    </div>''', '''<!-- component -->
<html>
    <head>
        <link rel="stylesheet" href="https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/css/main.ad49aa9b.css" />
    </head>
    <body>
        <div class="flex flex-col justify-center items-center h-[100vh]">
            <div class="!z-5 relative flex flex-col rounded-[20px] max-w-[300px] bg-white bg-clip-border shadow-3xl shadow-shadow-500 flex flex-col w-full !p-4 3xl:p-![18px] bg-white undefined">
                <div class="h-full w-full">
                    <div class="relative w-full">
                        <img src="https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/Nft3.3b3e6a4b3ada7618de6c.png" class="mb-3 h-full w-full rounded-xl 3xl:h-full 3xl:w-full" alt="">
                        <button class="absolute top-3 right-3 flex items-center justify-center rounded-full bg-white p-2 text-brand-500 hover:cursor-pointer">
                            <div class="flex h-full w-full items-center justify-center rounded-full text-xl hover:bg-gray-50">
                                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M352.92 80C288 80 256 144 256 144s-32-64-96.92-64c-52.76 0-94.54 44.14-95.08 96.81-1.1 109.33 86.73 187.08 183 252.42a16 16 0 0018 0c96.26-65.34 184.09-143.09 183-252.42-.54-52.67-42.32-96.81-95.08-96.81z"></path></svg>
                            </div>
                        </button>
                    </div>
                    <div class="mb-3 flex items-center justify-between px-1 md:items-start">
                        <div class="mb-2">
                            <p class="text-lg font-bold text-navy-700"> Abstract Colors </p>
                            <p class="mt-1 text-sm font-medium text-gray-600 md:mt-2">By Esthera Jackson </p>
                        </div>
                        <div class="flex flex-row-reverse md:mt-2 lg:mt-0">
                            <span class="z-0 ml-px inline-flex h-8 w-8 items-center justify-center rounded-full border-2 border-white bg-[#E0E5F2] text-xs text-navy-700 ">+5</span><span class="z-10 -mr-3 h-8 w-8 rounded-full border-2 border-white">
                                <img class="h-full w-full rounded-full object-cover" src="https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/avatar1.eeef2af6dfcd3ff23cb8.png" alt="">
                            </span>
                            <span class="z-10 -mr-3 h-8 w-8 rounded-full border-2 border-white">
                                <img class="h-full w-full rounded-full object-cover" src="https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/avatar2.5692c39db4f8c0ea999e.png" alt="">
                            </span>
                            <span class="z-10 -mr-3 h-8 w-8 rounded-full border-2 border-white">
                                <img class="h-full w-full rounded-full object-cover" src="https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/avatar3.9f646ac5920fa40adf00.png" alt="">
                            </span>
                        </div>
                    </div>
                    <div class="flex items-center justify-between md:items-center lg:justify-between ">
                        <div class="flex">
                            <p class="!mb-0 text-sm font-bold text-brand-500">Current Bid: 0.91 <span>ETH</span></p>
                        </div>
                        <button href="" class="linear rounded-[20px] bg-brand-900 px-4 py-2 text-base font-medium text-white transition duration-200 hover:bg-brand-800 active:bg-brand-700">Place Bid</button>
                    </div>
                </div>
            </div>
            <p class="font-normal text-navy-700 mt-20 mx-auto w-max">Notifications Card component from <a href="https://horizon-ui.com?ref=tailwindcomponents.com" target="_blank" class="text-brand-500 font-bold">Horizon UI Tailwind React</a></p>  
        </div>
    </body>
</html>''', '''<!-- component -->
<div class="min-h-screen bg-gray-100 flex flex-col justify-center">
  <div class="relative m-3 flex flex-wrap mx-auto justify-center">
                        <div class="min-w-[340px]flex flex-col group">
                            <div
                                class="h-48 md:h-56 lg:h-[24rem] w-full bg-red-500 border-2 border-white flex items-center justify-center text-white text-base mb-3 md:mb-5 overflow-hidden relative">

                                <img src="https://pixahive.com/wp-content/uploads/2020/10/Gym-shoes-153180-pixahive.jpg"
                                    class="object-cover w-full h-full scale-100 group-hover:scale-110 transition-all duration-400"
                                    alt="">

                                <div
                                    class="absolute z-10 border-4 border-primary w-[95%] h-[95%] invisible group-hover:visible opacity-0 group-hover:opacity-100 group-hover:scale-90 transition-all duration-500">
                                </div>

                            </div>
                            <a href="./single_post.html"
            
                                                    class=" block text-black text-center hover:text-primary transition-colors duration-150 text-lg md:text-xl mb-1">
                                Wild West Hoodie</a>


                            <p class="mb-4 font-light  text-sm md:text-sm text-center text-gray-400">Lorem ipsum dolor
                                sit
                                amet, consectetur adipisicing.</p>

                            <div class="flex justify-center gap-x-3">
                                <a href="/track_order.html"
                                    class=" px-5 py-2 border border-primary text-primary hover:bg-primary  transition-all outline-none bg-black border-black text-white hover:text-black hover:bg-white font-bold">
                                    Add</a>
                                <a href="/track_order.html"
                                    class="px-5 py-2 border border-primary text-primary hover:bg-primary hover:text-white transition-all outline-none bg-white border-black text-black hover:text-white hover:bg-black font-bold">
                                    View</a>
                            </div>

                        </div>
  </div>
    </div>''']
Hero = ['''<!-- component -->
<style>
@import url(https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.3.45/css/materialdesignicons.min.css);
</style>

<div class="min-w-screen min-h-screen bg-gray-100 px-5 py-5">

    <div class="w-full mx-auto bg-white px-5 py-10 text-gray-600 mb-10">
        <div class="max-w-5xl mx-auto md:flex">
            <div class="md:w-1/4 md:flex md:flex-col">
                <div class="text-left w-full flex-grow md:pr-5">
                    <h1 class="text-4xl font-bold mb-5">Pricing</h1>
                    <h3 class="text-md font-medium mb-5">Lorem ipsum dolor sit amet consectetur adipisicing elit repellat dignissimos laboriosam odit accusamus porro*</h3>
                </div>
                <div class="w-full mb-2">
                    <p class="text-xs">*Lorem ipsum sit amet</p>
                </div>
            </div>
            <div class="md:w-3/4">
                <div class="max-w-4xl mx-auto md:flex">
                    <div class="w-full md:w-1/3 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:my-2 rounded-md shadow-lg shadow-gray-600 md:flex md:flex-col">
                        <div class="w-full flex-grow">
                            <h2 class="text-center font-bold uppercase mb-4">PERSONAL</h2>
                            <h3 class="text-center font-bold text-4xl mb-5">$5<span class="text-sm">/mo</span></h3>
                            <ul class="text-sm mb-8">
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                            </ul>
                        </div>
                        <div class="w-full">
                            <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                        </div>
                    </div>
                    <div class="w-full md:w-1/3 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:-mx-3 md:mb-0 rounded-md shadow-lg shadow-gray-600 md:relative md:z-50 md:flex md:flex-col">
                        <div class="w-full flex-grow">
                            <h2 class="text-center font-bold uppercase mb-4">TEAM</h2>
                            <h3 class="text-center font-bold text-4xl md:text-5xl mb-5">$15<span class="text-sm">/mo</span></h3>
                            <ul class="text-sm mb-8">
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Elit repellat</li>
                            </ul>
                        </div>
                        <div class="w-full">
                            <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                        </div>
                    </div>
                    <div class="w-full md:w-1/3 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:my-2 rounded-md shadow-lg shadow-gray-600 md:flex md:flex-col">
                        <div class="w-full flex-grow">
                            <h2 class="text-center font-bold uppercase mb-4">PRO</h2>
                            <h3 class="text-center font-bold text-4xl mb-5">$35<span class="text-sm">/mo</span></h3>
                            <ul class="text-sm mb-8">
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                                <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Much more...</li>
                            </ul>
                        </div>
                        <div class="w-full">
                            <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="w-full mx-auto bg-white px-5 py-10 text-gray-600 mb-10">
        <div class="text-center max-w-xl mx-auto">
            <h1 class="text-5xl md:text-6xl font-bold mb-5">Pricing</h1>
            <h3 class="text-xl font-medium mb-10">Lorem ipsum dolor sit amet consectetur adipisicing elit repellat dignissimos laboriosam odit accusamus porro</h3>
        </div>
        <div class="max-w-4xl mx-auto md:flex">
            <div class="w-full md:w-1/3 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:my-6 rounded-md shadow-lg shadow-gray-600 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center font-bold uppercase mb-4">PERSONAL</h2>
                    <h3 class="text-center font-bold text-4xl mb-5">$5/mo</h3>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                </div>
            </div>
            <div class="w-full md:w-1/3 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:-mx-3 md:mb-0 rounded-md shadow-lg shadow-gray-600 md:relative md:z-50 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center font-bold uppercase mb-4">TEAM</h2>
                    <h3 class="text-center font-bold text-4xl md:text-5xl mb-5">$15/mo</h3>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Elit repellat</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                </div>
            </div>
            <div class="w-full md:w-1/3 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:my-6 rounded-md shadow-lg shadow-gray-600 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center font-bold uppercase mb-4">PRO</h2>
                    <h3 class="text-center font-bold text-4xl mb-5">$35/mo</h3>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Much more...</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                </div>
            </div>
        </div>
    </div>

    <div class="w-full mx-auto bg-white px-5 py-10 text-gray-600 mb-10">
        <div class="text-center max-w-xl mx-auto">
            <h1 class="text-5xl md:text-6xl font-bold mb-5">Pricing</h1>
            <h3 class="text-xl font-medium mb-10">Lorem ipsum dolor sit amet consectetur adipisicing elit repellat dignissimos laboriosam odit accusamus porro</h3>
        </div>
        <div class="w-full md:flex mb-5">
            <div class="w-full md:w-1/4 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:my-6 rounded-md shadow-lg shadow-gray-600 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center font-bold uppercase mb-4">PERSONAL</h2>
                    <h3 class="text-center font-bold text-4xl mb-2">$5<s2an class="text-lg">/mo</span></h3>
                    <p class="text-center font-bold mb-5">
                        <a href="#" class="hover:underline hover:text-gray-700 transition-all transform hover:scale-110 inline-block">Read more<i class="mdi mdi-arrow-right-thick ml-1"></i></a>
                    </p>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                </div>
            </div>
            <div class="w-full md:w-1/4 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:-mx-3 md:my-3 rounded-md shadow-lg shadow-gray-600 md:relative md:z-50 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center font-bold uppercase mb-4">TEAM</h2>
                    <h3 class="text-center font-bold text-3xl md:text-4xl mb-2">$15<span class="text-lg">/mo</span></h3>
                    <p class="text-center font-bold mb-5">
                        <a href="#" class="hover:underline hover:text-gray-700 transition-all transform hover:scale-110 inline-block">Read more<i class="mdi mdi-arrow-right-thick ml-1"></i></a>
                    </p>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Elit repellat</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                </div>
            </div>
            <div class="w-full md:w-1/4 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:-mx-3 md:mb-0 rounded-md shadow-lg shadow-gray-600 md:relative md:z-50 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center font-bold uppercase mb-4">PRO</h2>
                    <h3 class="text-center font-bold text-4xl md:text-5xl mb-2">$35<span class="text-lg">/mo</span></h3>
                    <p class="text-center font-bold mb-5">
                        <a href="#" class="hover:underline hover:text-gray-700 transition-all transform hover:scale-110 inline-block">Read more<i class="mdi mdi-arrow-right-thick ml-1"></i></a>
                    </p>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Much more...</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Buy Now</button>
                </div>
            </div>
            <div class="w-full md:w-1/4 md:max-w-none bg-white px-8 md:px-10 py-8 md:py-10 mb-3 mx-auto md:my-3 rounded-md shadow-lg shadow-gray-600 md:flex md:flex-col">
                <div class="w-full flex-grow">
                    <h2 class="text-center text-3xl font-bold uppercase mb-2">ENTERPRISE</h2>
                    <p class="text-center font-bold mb-5">
                        <a href="#" class="hover:underline hover:text-gray-700 transition-all transform hover:scale-110 inline-block">Read more<i class="mdi mdi-arrow-right-thick ml-1"></i></a>
                    </p>
                    <ul class="text-sm px-5 mb-8">
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Lorem ipsum</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Consectetur</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Adipisicing</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Sed do eiusmod</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Aliquip ex</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Excepteur</li>
                        <li class="leading-tight"><i class="mdi mdi-check-bold text-lg"></i> Dolor sit amet*</li>
                    </ul>
                </div>
                <div class="w-full">
                    <button class="font-bold bg-gray-600 hover:bg-gray-700 text-white rounded-md px-10 py-2 transition-colors w-full">Enquire Now</button>
                </div>
            </div>
        </div>
        <div class="text-center max-w-xl mx-auto">
            <p class="text-xs leading-tight">*Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aliquam eligendi officiis, impedit ducimus eaque a corporis, dolore quia officia quam tenetur suscipit dolores, quos, quaerat quo provident iusto. Eius, impedit!</p>
        </div>
    </div>
</div>

<!-- BUY ME A BEER AND HELP SUPPORT OPEN-SOURCE RESOURCES -->
<div class="flex items-end justify-end fixed bottom-0 right-0 mb-4 mr-4 z-10">
    <div>
        <a title="Buy me a beer" href="https://www.buymeacoffee.com/scottwindon" target="_blank" class="block w-16 h-16 rounded-full transition-all shadow hover:shadow-lg transform hover:scale-110 hover:rotate-12">
            <img class="object-cover object-center w-full h-full rounded-full" src="https://i.pinimg.com/originals/60/fd/e8/60fde811b6be57094e0abc69d9c2622a.jpg"/>
        </a>
    </div>
</div>''', '''<!-- component -->
<script defer src="https://unpkg.com/alpinejs@3.2.4/dist/cdn.min.js"></script>    
    
<main class="grid w-full min-h-screen text-gray-100 bg-gray-900 place-content-center">

    <section x-data="skillDisplay"
        class="p-6 space-y-6 bg-gray-800 rounded-xl md:grid md:grid-cols-2 md:gap-4 sm:space-y-0">
        <div class="grid grid-cols-2 gap-6">
            <template x-for="skill in skills">
                <button x-text="skill.title"
                    class="px-4 py-2 text-xl text-gray-100 transition bg-blue-600 rounded-md h-14 w-44 hover:bg-blue-700"
                    :class="(currentSkill.title == skill.title) && 'font-bold ring-2 ring-gray-100'"
                    @click="currentSkill = skill"></button>
            </template>
        </div>

        <div class="flex items-center justify-center" x-data="{ circumference: 2 * 22 / 7 * 120 }">
            <svg class="transform -rotate-90 w-72 h-72">
                <circle cx="145" cy="145" r="120" stroke="currentColor" stroke-width="30" fill="transparent"
                    class="text-gray-700" />

                <circle cx="145" cy="145" r="120" stroke="currentColor" stroke-width="30" fill="transparent"
                    :stroke-dasharray="circumference"
                    :stroke-dashoffset="circumference - currentSkill.percent / 100 * circumference"
                    class="text-blue-500 " />
            </svg>
            <span class="absolute text-5xl" x-text="`${currentSkill.percent}%`"></span>
    </section>
</main>

<script>
    document.addEventListener('alpine:init', () => {
        Alpine.data('skillDisplay', () => ({
            skills: [{
                    'title': 'HTML',
                    'percent': '95',
                },
                {
                    'title': 'CSS',
                    'percent': '70',
                },
                {
                    'title': 'Tailwind CSS',
                    'percent': '90',
                },
                {
                    'title': 'JavaScript',
                    'percent': '70',
                },
                {
                    'title': 'Alpine JS',
                    'percent': '80',
                }, {
                    'title': 'PHP',
                    'percent': '65',
                }, {
                    'title': 'Laravel',
                    'percent': '75',
                }
            ],
            currentSkill: {
                'title': 'HTML',
                'percent': '95',
            }
        }));
    });
</script>''', '''<!-- component -->
<style>
    .juice {
        background-image: url('https://i.ibb.co/SN2Sp4T/juice.png');
    }

    .juice2 {
      background-image: url('https://i.ibb.co/yyMXMSF/juice2.png');
    }
 
    .juice3 {
      z-index: 10;
      position: relative;
    }
 
    .juice3::after {
      content: '';
      position: absolute;
      opacity: .2;
      z-index: -999;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background-image: url('https://previews.123rf.com/images/olgasiv/olgasiv1403/olgasiv140300026/27343111-image-en-noir-sur-un-fond-blanc-dessin-de-l%C3%A9gumes-de-fruits-et-de-baies-.jpg');
    }

    .text-primary {
        color: #f9b529;
    }

    .text-primary-lite {
        color: #fac251;
    }

    .text-secondary {
        color: #294356;
    }

    .text-secondary-lite {
        color: #d5dee5;
    }

    .bg-primary {
        background-color: #f9b529;
    }

    .bg-primary-lite {
        background-color: #fac251;
    }

    .bg-secondary {
        background-color: #294356;
    }

    .bg-secondary-lite {
        background-color: #d5dee5;
    }
</style>

<div class="h-screen bg-white">
  <div class="juice3 bg-gray-100 bg-opacity-90 py-10">
    <div class="container mx-auto px-4 flex flex-col lg:flex-row">
      <div class="juice relative lg:w-2/3 rounded-xl bg-secondary-lite bg-cover p-16">
        <p class="max-w-sm text-secondary text-4xl font-semibold">Active Summer With Juice Milk 300ml</p>
        <p class="max-w-xs pr-10 text-secondary font-semibold mt-8">New arrivals with naturre fruits, juice milks, essential for summer</p>
        <button class="mt-20 bg-white font-semibold px-8 py-2 rounded">Shop Now</button>
        <div class="absolute bottom-5 right-5 flex">
          <a href class="h-6 w-6 flex items-center justify-center rounded-md bg-white">
            <svg class="h-3 text-gray-700" aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-left" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" class="svg-inline--fa fa-chevron-left fa-w-8 fa-3x"><path fill="currentColor" d="M231.293 473.899l19.799-19.799c4.686-4.686 4.686-12.284 0-16.971L70.393 256 251.092 74.87c4.686-4.686 4.686-12.284 0-16.971L231.293 38.1c-4.686-4.686-12.284-4.686-16.971 0L4.908 247.515c-4.686 4.686-4.686 12.284 0 16.971L214.322 473.9c4.687 4.686 12.285 4.686 16.971-.001z"></path></svg>
          </a>
          <a href class="ml-1.5 h-6 w-6 flex items-center justify-center rounded-md bg-yellow-400">
            <svg class="h-3 text-gray-700" aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" class="svg-inline--fa fa-chevron-right fa-w-8 fa-3x"><path fill="currentColor" d="M24.707 38.101L4.908 57.899c-4.686 4.686-4.686 12.284 0 16.971L185.607 256 4.908 437.13c-4.686 4.686-4.686 12.284 0 16.971L24.707 473.9c4.686 4.686 12.284 4.686 16.971 0l209.414-209.414c4.686-4.686 4.686-12.284 0-16.971L41.678 38.101c-4.687-4.687-12.285-4.687-16.971 0z"></path></svg>
          </a>
        </div>
      </div>
      <div class="juice2 mt-6 lg:mt-0 lg:ml-6 lg:w-1/3 rounded-xl bg-primary-lite bg-cover p-16">
          <div class="max-w-sm">
            <p class="text-4xl font-semibold uppercase">20% sale off</p>
            <p class="mt-8 font-semibold">Syncthetic seeds<br />2.0 OZ</p>
            <button class="mt-20 bg-white font-semibold px-8 py-2 rounded">Shop Now</button>
          </div>
        </div>
    </div>
  </div>
</div>''', '''<!-- component -->
<div class="contenair bg-cover min-h-screen w-full flex justify-center items-center"
style="background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1124&q=100');'">
  
<!-- card -->
  <div class="w-1/2 bg-white p-5 rounded-xl bg-opacity-60 backdrop-filter backdrop-blur-lg">
    <div class="header-card flex justify-between font-semibold">
      <div class="">Team members</div>
      <div class="flex items-center gap-x-1 text-sm text-blue-500">
         <svg class="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <path fill="none" d="M0 0h24v24H0z" />
          <path d="M1.181 12C2.121 6.88 6.608 3 12 3c5.392 0 9.878 3.88 10.819 9-.94 5.12-5.427 9-10.819 9-5.392 0-9.878-3.88-10.819-9zM12 17a5 5 0 1 0 0-10 5 5 0 0 0 0 10zm0-2a3 3 0 1 1 0-6 3 3 0 0 1 0 6z" />
        </svg>
      <span>See all</span>
      </div>
    </div>
    <!-- end header -->

    <div class="card-content divide-y flex flex-col gap-y-3 mt-5">

      <div class="card-content-profil flex justify-between items-center">
        <div class=" flex gap-x-2 items-center">
          <img class="avatar h-10 w-10 rounded-full border-4 border-opacity-40" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAASABIAAD/4QCuRXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgExAAIAAAAhAAAAWodpAAQAAAABAAAAfAAAAAAAAABIAAAAAQAAAEgAAAABQWRvYmUgUGhvdG9zaG9wIDIxLjAgKE1hY2ludG9zaCkAAAADoAEAAwAAAAEAAQAAoAIABAAAAAEAAABAoAMABAAAAAEAAABAAAAAAP/hC1lodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDYuMC4wIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RDM4NzEyOTk1NEU1MTFFQkE5NUFBNDNDN0ExMTE5QUMiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RDM4NzEyOTg1NEU1MTFFQkE5NUFBNDNDN0ExMTE5QUMiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3NTAxMDgwNDEyMTAxMUVBOTNGNUU1NkMyNEY0RUY2MCIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjEuMCAoTWFjaW50b3NoKSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjUzZDhlNGZmLWRkMDctNDQxZC04ZDlhLTRhNjcxYmI5OGMzNyIgc3RSZWY6ZG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjY5ZWQxZGVkLTZmNzYtNWM0MS1iZGIwLWU0OWNkMjVjYzhlMyIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8P3hwYWNrZXQgZW5kPSJ3Ij8+AP/tADhQaG90b3Nob3AgMy4wADhCSU0EBAAAAAAAADhCSU0EJQAAAAAAENQdjNmPALIE6YAJmOz4Qn7/wAARCABAAEADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9sAQwAQCwsLDAsQDAwQFw8NDxcbFBAQFBsfFxcXFxcfHhcaGhoaFx4eIyUnJSMeLy8zMy8vQEBAQEBAQEBAQEBAQEBA/9sAQwERDw8RExEVEhIVFBEUERQaFBYWFBomGhocGhomMCMeHh4eIzArLicnJy4rNTUwMDU1QEA/QEBAQEBAQEBAQEBA/90ABAAE/9oADAMBAAIRAxEAPwDqZJ5WDQwHzH6PIcBU+mOp9qjjslVAuTwOuaoxaxsQKLXGOwIxTjrF0T8kCge55/QVSjVWysckcbQb+OLb0RNNG1oDLuzCBukBP3QOSRXKaj40uJHMdlGixA8NL8zsv+5kYB+ufxrZ1y4e8hjsXcCKYGS42ZBMaEAJnr8zHn2BqG3sdIWARiziIQ5JcBmLepY5JP1qJTTeq1XdWOyNNyV+j2s7mdpnigXEi208caSyEKsysdu48fODyo9OT6V0VsdMtW3uS9xk7pNpznuB7Vzupx2eNojiRDwCo29Ochh39xWlpkF7f2xlAEjRsY3YkAkgAhsYxyDWkKikuVuyXY5cZGvSUZUYKprZprbs0ac+oW0+IIy2ZCF5BA5PNWruRYowg6nisMq9pqVtFOu1i24854ANahY3D+aQdmTs9CB0P41ckox5uiTfzJw8q0oXqx5Zyla1rWR//9CyFYnH9asx22V3M2PTn0pqzRxjbv8AfpVGNW1GF5HuHHJCKo2gAHH1rpk3taxz0OHo06i9tL265ZPkjFx287+ZJqCJDKskR81thDKp3Mecjgc4rE87VLm8Xy2d0J2hMbVTJx90ccepqzHLFp8jOVbcPvFs9B6E1f8A7WWZVktxAsytzDKxXPGQflBOfY1wVk1Ulpe6WvTY9KnThCMYRTpRhoodVb1MqS3uorx1ulLdVTA3DPqRg8cY4rY0mK9MDQQ/u5i4B54GR149AKgOqOvnS3ZhWZz8kcZJ575z/StLwnMJYLu6bhg+1fYbQT/OnRvzLToKq+VNpptvqk7X33KerWRW9tbaFme6kyGlYlmPHJPoBW9PGI7dLdTtbbtBHtUWmRLcTyanJ1OY4M9kB5b8SKlnBebd6V01Z+7Gn1jq/X/gHDUi2rJfE+X5Pc//0ZwY3lVOV3cZJ6ZqlHfW9g728gBjViBKrfL171chFxMypDEGJ6kjgD3J6VoQWFrZxebcbHlH8RAVQfRQf510TduW2rtstWexXk4SUk0rXVm9LO25Su7UXdi4aMrG6/I54YHswB965OC7NuHjcIJC3zs65De4PUV3F1eW6qhaTLDngbh6kHHY1xus6TLFcSGMb4yx2+u1vmUe/B+tY1Yz0lKLins7W/E5Kk1WlejKFScF70IPmkl6asqz3QY/JsLkj7q4ArpNJivl04QWRULKm+eRzyJMZbA9+3pXM2ljPK4AQgk43NwB+ddXp91a2qBd2AvBOCR6dQKrDxnzNwg6llrpcy5IWbryhSUl7jm+W7T6XtfzOitVkisow4C/KAqjoBUbTJk4OWHUVFFqMUwCrMGOOOecfQ0yOQebKjKVbrz/ABD+8D6VCpz9pUlUXLouRfm3czkrcnLy1IXd5xd15ao//9KxDqMkUTwodhUDJP3iR1696qzyyXWFyZHZkVe+M5c/pUdzcwyfMDh88N647Gp7G4ieQkYWNf4R/wB88/lgev0rvWLowipQh773Xa3n1RpLJsVUqyVevenFOSlu5Nv+XZPuSm3upeI48IoxubAH4VHc2lwyRncqPGvlsQScgcpxjsOKvy3sSjl1X8QMfQVV+020sixeai7jtBJyMnoOPfvUPE15LSCsv7rfrcunlmDpPmnVkmtdZqL07Ws7lRbSRUdjIu9xsjGMAZ++xx3xwKiSxuM4AUn+5nBI9sipRe2+TukXdnBx04449qlW+tjgNIrDtk8/nVU62JgtKdk+iptL8LHRXwOX1nepX5pW+J1lJ/8AkzZQdJ4SUZG7tGeowPvA4zyKng1OaPbGzbgG4B5I7cd/wqS8uoXiMkbhmj+YEEEnHr+HFZRv0dw/VhkA/j1NU8bdONamtrrpr6M5pZNBcssPiGuZpO7T06u6tf0sf//Z" alt="" >
          <div class="card-name-user text-xs">
            <h3 class="font-semibold">Chris Wood</h3>
            <div class=" flex items-center gap-x-1">
              <span class="h-3 w-3 rounded-full bg-green-500"></span>
              <span>Online</span>
            </div>
          </div>
        </div>

        <div class="card-action">
          <button class="flex items-center px-2 py-1 text-xs text-white bg-gray-500 hover:bg-gray-600">
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
            <span class="">Invite</span>
          </button>
        </div>
      </div>

      <div class="card-content-profil pt-3 flex justify-between items-center">
        <div class=" flex gap-x-2 items-center">
          <img class="avatar h-10 w-10 rounded-full border-4 border-opacity-40" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAASABIAAD/4QCuRXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgExAAIAAAAhAAAAWodpAAQAAAABAAAAfAAAAAAAAABIAAAAAQAAAEgAAAABQWRvYmUgUGhvdG9zaG9wIDIxLjAgKE1hY2ludG9zaCkAAAADoAEAAwAAAAEAAQAAoAIABAAAAAEAAADAoAMABAAAAAEAAADAAAAAAP/hC1lodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDYuMC4wIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RDM4NzEyOUQ1NEU1MTFFQkE5NUFBNDNDN0ExMTE5QUMiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RDM4NzEyOUM1NEU1MTFFQkE5NUFBNDNDN0ExMTE5QUMiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3NTAxMDgwNDEyMTAxMUVBOTNGNUU1NkMyNEY0RUY2MCIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjEuMCAoTWFjaW50b3NoKSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjUzZDhlNGZmLWRkMDctNDQxZC04ZDlhLTRhNjcxYmI5OGMzNyIgc3RSZWY6ZG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjY5ZWQxZGVkLTZmNzYtNWM0MS1iZGIwLWU0OWNkMjVjYzhlMyIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8P3hwYWNrZXQgZW5kPSJ3Ij8+AP/tADhQaG90b3Nob3AgMy4wADhCSU0EBAAAAAAAADhCSU0EJQAAAAAAENQdjNmPALIE6YAJmOz4Qn7/wAARCADAAMADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9sAQwAQCwsLDAsQDAwQFw8NDxcbFBAQFBsfFxcXFxcfHhcaGhoaFx4eIyUnJSMeLy8zMy8vQEBAQEBAQEBAQEBAQEBA/9sAQwERDw8RExEVEhIVFBEUERQaFBYWFBomGhocGhomMCMeHh4eIzArLicnJy4rNTUwMDU1QEA/QEBAQEBAQEBAQEBA/90ABAAM/9oADAMBAAIRAxEAPwAkhDc9abFHtPFSo6tx3p0i7BmvMjJpnY1cgkDbqgmtmYgg1Oz45NLuLDFXd3E1oZ8sTKMelT2UO/gjJFTSwnHNS6aApYsPatKMrySehnUTUXYr3IkixGoxmksrYB90h5NW79gzgKOFHX3pbWBtm5jzVVG3Oyd0KCSjd7skeOMDjtVWQpzTp59rlc1AxBb2rCafMax2IZCcnAqNY3wSKs/LitHTbNJhlhV005OyIm1FXZiIh3fN+tWo3jQ+wrU1WwtooHcYXaM5rnLaTe2RyufzrSpRkrLf0JhUT12sbC2b3WDj5e1alhphh6/hRpkiGME/lWqrpiumnTUErb9zCc3NvsMWPb1NOAGaimnVc81Ua+COo3da0IL0tuJByaovIlnJtPCnvUwvWZfk+YetRT7ZV/eUITJBdQydDmqOplfJyBxQsW1vk59KdcR5iAfgVaViWzGtLhcufSq2u3avHswOn40+7jEKNKmQM1h3lwZSMnpSbsi4xu01sj//0KNnM2dzdK0fMMgrGtixAXoO5rQNzHCgXPJrhlHXY60yUxbjU6xBRVZblVGWp5uwwwKz1vsPcfI6jOaijnRWJBx604ReaKqXduY4yQeaI2btdq4mTvdwFsZqyt0oj4IrlC7Bzg81q2UUkkeXJroUY01d63Id5abDp5fMlzTjKip15qK4UITjk0Wmm3t62YkOz/noeEH49/wpfFstw23Y+BjJJitRbprSPKc4pbXQWiP79wT0Coev1yKv/wBj2rD5/MP+yWx/6DWtODjdpa9LmdRqVtdDlNV1C+vhs5WLuB3punIyBd46V1p0fTwNvk5/2t5DD8ajn0a3kUm2PluOq9s/0qn7S19GxJR22RnxXwiGAeTUi6u69Dn61kXiTW0pjkUqw7f1qETg9aXtZ28xeyjc07jU5GbIY571VNy8j5Y1Ta4FMSYlhzU+8927FWilojstPwLZSeeKoX2oospRexqtb6lsg2k8gVmTSl5C3c1s5pJW3Mow1u0dJYXSu4B7VZ1KaNLc5PJ4FcxaXLxPkGpb+/eUBCeKFV77mjop7aItXhiezJJHA6Vx8x/eEDpmtqaYiDBrEc5kJ96pyvYiMeW5/9HK2snSo/mMoLHilkuQDgU1phtz3rmV+x0NouXO0xAL+dPsIg3LfhWSt2S3J49KsJfNGQVOBQ6b5bC51e5tu4tx7VRubsSKRVK51JpFC1Aj7u9QqLWr7le0T0RHhRLk9K0F1FI0CJ6VlXBIPWo7RXnuo4UBZnYDC8n3P4CtvZqS16Ec1tjptJ09r+YTTgG3XnG7O8j+HA7ev5V06DaoQYUKOFUcAewqlbiKzt44UG1UwoXOTz3J9TRLemKUj36H+nsa0jFRRLvJltpMc5wR+RPSobi8WIbieVVmPrwM1mXN4ckgkgjt1yOeR6j1rMur5pcZPJBHp14P502xqHc1ZdcQ3IQH5SQc+w6mpH1NY3Vd2Xdxkei8kk/hzXKuTuD55HU/rR9ok3uvduPwzjr9KVynFHQ/2haagmyVVLAlV3D0NZk2kytlrZS3J+Tgnj0Of51UhwgJIKrnLKxyuf7wI+ZT7jI9a0rW/MEg3ncjj5GJ6+xI647H8KHZ7/eJxtsY80MkblJVKOOqsMH9aRFIrfvGhv4WRwPPjUtC468dV+h/+vWIwKCpatp32JsTIeKZ/FzUImIHWmvPjvRyjuXk2jpUVw3z1R+1sDTWuCzc0+UfMXLogwj6Vkj71X5ZAYsVRUbmxVImWrP/0uX3ktmnl8ioAwpBJis7FtiFsNTw/FQO+TmgPxVkslLUqylah30m6lYCSWQtWh4bCrdSzMM7EAHOOXb/AOxrKJq9pMhja4wcZRR/48eaaKWrVzpnuxM6xoAwLAdcDr2/GrMgD5dsru5wRnFZmk20lxMkj/cUg4B6Y6DNbtxECOBnHp29qDRWRjzROSTGcZ6ngD8cmsy4Voyd7K57gZI/OtaaznZvvfL6U37AoADjgUi7eZhlTLwqH+n61atNPlZwWGPWtiO2hUcAfWrMaIvNFg0RSfT18krjkjrWBcJc2suxfmQk4UgEV17spGBWLqtvmMsozjkc4/UUWE9ULpS+cAJflkUZQHnAIGR696ybqbBZOMqSDjOBgkY5qzpl5tfzHIDgEY7Z6CqGojN7N7uSPx5ptJ28jJkBkyaY2e9KFwaUigQzFIOtPwKaaAFdjjFNi4YUMc0JwaYdT//T43dSZptKKRQ00U4ik20CEopcGkpgKDViykCvIuOXXAz2IOarU+HIkDDoCAx7DdwMntmkNbnb6UuxEIPy+3c+ua0Xc59vQVR0lw9lGR6YP1HBqW5uorZN0zBfQfxH6Cmaj2I65/WoGfPY5+tVV13TGP3j9SD/AEqzHe2k65jYMDSsUmhhc9lJ/T+VKokPYL+pqTfCAT6VSu9atbf5Scn0Wiw7lkhgckkfkB/KopVLgqTnNZLa5dzMfIjGztuH+NWrTUWlcRzQmJz0IOVb/Cgm5j3MDW1zsb7rEMPpmq7sXdmPJJzWtrMTy3EKRKWcqx2jr1A7/WqV9p01j5fmSI5kBJCEnaRjg5+vWghopnihQTQaeuBQSxNtMC5NPZ6aGoENkXBoXFK5BFMzQFz/1ONC5pMYq75GDTTb1Ny7FQilGKna3ameQc0wsR8UwLlsVY8g0CIg5ouFicWA8sNWvopkitbizeMS2rguyEc88Nz3yKyhdEIFq7pN3JvnSPO/yXZf+Alc/wA6C4JcyVlq7am1paLbmeAcRB98IOc7WGSDn3zWbfRxNJ58ymV35XI3HHbAPA9q0LSwju7HdeIsztv8pnGWAbrz6ZqWe0jmjEh4BAz6/T8DTWqKtaTXRM5O82A/vAqn+6HUsD6YUY/WmWsgjbKyYXqSeMfX2q5fWiYEfllQhyNnA9PSobbTnlWRY1IJGMk5xnjH40WE7p3si+8svkGXbKY8Z8wRsUx6ggcj3rHmZS5Y/MT0B967yYItiVJ4CYP1xiuMlsnjGSAdpwT1xiiwSbejK6ShG2PvVu20KRz6g8mtOy3v8yjDqMjsCR6j3qG3tzK4Ylcj+Lv+FbUcCpFlcbyMD6npQHT8jPleYyrPIghLrtjy25sHk528D86qan8rouc5BbP1C/4Vr3lusyLGnMi8J/n8Kw9Uwsyxq2/ZGqkj1GSf50mtSpaU7dW9Si7YpQ5xTSCaAKDACSaBSmkFAwNNzzT8ZpDGaBWP/9XLa0OeopfsbeorPa9uAeRV23+0zJnFLkNOYDZSH7uKjawm9MVejS4XqDTpZJFHQ0+RC5zPFjLjkVGbSSr3nSMMYpmybOSDRyj5ii1m5Gam05ZbO8jnHAB2v/uNw3+NTGKcnp17VetLBYoXvL8ERqcJEfl3n3zjj+dOwubU11lgEpih6YJwPujHp9c02V1TcR0b7y+/qD796WGJfKW4kVI5GG2JIxgAHkjPfgVTmfMmyk9DWNpd9CvcW5nb/WlVPbaf5jj9aktY41lSGIYjTkk9Wft07DrU6qAuelVDczW3m3McBm2jCgHGBn5m5pXLUV5u3c17lAYCvbHNc5LmK8ZcZB4ZW+6wGcEf4ii68RzvgIgUEd+v0qKOW4vtsjqFZCdvrg//AKqLiSWz1LaR26fOsXP++f8AD+tK14ScAADsBTd2BgjnvUJQbs0XY+VIfJftbz88rtUlfXINYzq0js7dWJJ/H/Crt0rtMxXoMD8hUBSQdqDKUr/IgMPHSmeUfSrflyHtSCKSixOhV8k+lHlVb8qT0pPKkosGhVERFOCVY8qSgRuTiizDQ//W5tpYy3atC01CKJcVh7Hp6wSnkVVx2OhOrRetQT6nGwwDWP8AZpvegWs7MEUFmY4VQCST7AUXCyNJNQUGtnTLWe/US48u37SH+L/cHf69Ki0fwkoCz6p8zdRbDoP+uhHX6Dj610YkhUhF/h4CJ0GO3HAoF6BDb2tom4KB23HlmPpWZq94jxuABwGCkgHBx/CP61JqEsmMiTDngAfwr6L9e5rKlLCM5+8c++B70yorqE+oKn2R8/KpUNzxjGD/ADzVrYDJurmp5i8CoTwhK+vHStqzvlkt43PUqA3+8OD/ACqGbQ7F58Zx2FRSXUHlsGZUjHBJNVbu5fy2Cdx1FY/k22AZy7HqcMR19MdKm5QtyLOSfzEc4Xn7uAfYZqaK+tVAAyh9+n5iqEiaaDwZBz0Jz+tKjWY4jhz/ALTc0w/8B+TuaiXCTcg5p5I6Vnw4DEgAZ/CrIc9e1CFfQ3oUsby2jE67JFUKJFGDx0z1qnd6TcwAyQgXEQ5+T74Huv8AhVeGYpEpySQenTH0q9FqDRuoOeehzVmDT1Mb7ZEMjuOCO4PoR2o+2Q1v3llp+pridds2PlmTAcfj3Hsa57UPDl7aZdD58H99ByB/tL/UUCHfbYfagXkHtWX9mkoFtJSGa32u39qha9hDZFUPssvrTDbyZxRcD//X5Iyjd7VoQTw7OetZQYZp4fA68Dnii5VjctY2vJhDbruc888AD1J7V1GnaVbWI8zh5yPmlPb1C+gqtoumiysEWQAzygPKevJ5C/RRxVuZzGgWPAJ9scetUTuFzcAv5ZJ2dwOM/wC93/D86Y0iBOenYVT3NnEuSD0kxyD/ALX+IqvPdtbthyGUjIbt+fNMdht0A8vmBiwHqen59hVeQ7l65Xqff61PO6SxiWM5P8Xt9aoFyQVzn0pFoyJmKySJ23ZA7c+1T2MpUNF2b5h9e9Vrridvwz+PFKjMoBHUHP8A9aoKTszRFyRlZOV9e4qdLe2lGWII781lvLkZqNpvQkH1FIvmL15BZJ/q06frTYfsgXJABrOLMerE0+Mdzz9aBc3kXC4ZsJwvrTw/JA6KAMfqarGRYxuanRn5Mt95uSPrTRLZbWT5FHvkf4VM8mZkGeQOfWqkZJfPYU4SEXWB0AAqhGvBPlxg/wCfWtSGcnB9qwhIE+Y8Cr0U+VHfPQiqRDRLqGjw3amW2xFc9cfwP9R2J9a5eaWWCVoZl2SIcMp7Guy8zYg3HBbuax/E9oJrVb1B+8iO1z6oeM/geaTXUWxg/bKRbnnJqpnHWl3VNxn/0OLrQ0Oz+2anBCwyinzJP92PB/8AQsVRxmun8IwbI7m6I5ZljU+yjcf1ahasbOldwoJPQVUmm3d+OeRSTyEkYP49fwAqm8hBO7gH/PSrBIJJ2U7l59c9DVaQxTRtjmPuh6oe7L7e1I8rgZ6j1qsZQr7sdeuPWgpDYZ2jYxuMno3PUf56VEx2uw6+hPp2NRXL7JBIowOh+nrSyvwrDBxxx6GpKKF2P9Jwe4INMiPr1HBpbw4dCO2ajYlXz/e5/wAaQupK4ONy/iP8KiLipQQeh/Ch0ib7w59R1oGRBhUgkUDOaZ9mBPyyD8Qf6U9LVc/PJx6KP6mlYLvsJCrzy7j9xeT6fSrLPx/KlUoq7UGFH+eajf5jx3pgTw5AzmmwHfcsfegNtQ9j0qO2OJTxnPagDSmb5QM/jV6xzhSTwKy5WDOoqz9pEMHHcc1SF0Lrz+fciMHKqeT1qd5VlkNu2DDtKkeuRg5rKtZGSJpjwTUlvKWbd3/r600xNHO3MTQTyQn/AJZsV/AdP0xUVaOuJi/Zv+eiq349D/Ks+oejEf/R5ONVIya7LSoPsmlQoRhmBkb6ud39a49F7HuCK7aKTzbO3kOPmjQ8dORTh1Y3uiGWQc54/DjiqjyEnnnP6fh1qSaRT14x689fWoHZW+7wR17H/JqiiOTLDPP+frVW5iZeV47+36U5pirZ/LI4xT45IpMq/Ge4/nSGijIPMRhg8jINQxPvt8HquR+VWp4GhbcMtGfut7VSX5JZE7EhvzpDIbnnbTG5iVv7v9allGRj0FRx8xsvtmkKw6MBx7ilO8defeoom2tVrG8ZoGiEMO4NPU+xNKY6cAAKAA5xzSIMnIobpTouBmgBXPFJbn58mmuevNLExALelAE+/dKT0x0odjLIsfp8zH2qsj5p0cvzE9hxn6UwLzyHhFPHp2qzEQij1PrVGJtoMr9O1TwuzkyN07CgRW13mWBvWM/oR/jWZWlrOWFu/qHH6g1nAcUpbk2P/9LnEK7cdwM1q6brVv8AZxaXBEbRLtjc/dZeijPYjOPesUgqCTVNznNVF+78xte9fyOumIOGAB77v/1VTaVkOcZHoP6fSsCG6uYBiKRlX+71X8j/AEq0urSkYlXPqynH6H/GlcpNF6V94+Y8f57VSlEifMp+WnrfwEdceob/ABpWeKQZVhk0FIjjvriDhiHjbgjqKR2V5w6cBl/lULhcmPPB/Q02Aktk/wAIwKQEh5zUcP3yKeDyaZF/rKAIiMGrUDcetQSLg/jToDzQIsydeP1poHH1qQ5IyKQjB5pjI298YpxICD3pvXrTZWG4DNIAPIoJ2xE+vFNBzTJn6IPqaAHIcLuPTGadEo2gvwg7dyaidgqgfpSCVWbMuSB0UcCgV0XIyZnz0RfyFWvNLkRpyo/z2rN+15ATBWMdlqVb+OMYjQk++B/jTC6LWr4+yQeocj81NZYJx0qSe4ln2mToOijoBWpp9mk8eAKLcz0IcktWf//Z" alt=" alt="" >
          <div class="card-name-user text-xs">
            <h3 class="font-semibold">Jose Leos</h3>
            <div class=" flex items-center gap-x-1">
              <span class="h-3 w-3 rounded-full bg-yellow-500"></span>
              <span>Busy</span>
            </div>
          </div>
        </div>

        <div class="card-action">
           <button class="flex items-center px-2 py-1 text-xs text-white bg-green-500 hover:bg-green-600">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
            <span class="">Invite</span>
          </button>
        </div>
      </div>

      <div class="card-content-profil pt-3 flex justify-between items-center">
        <div class=" flex gap-x-2 items-center">
          <img class="avatar h-10 w-10 rounded-full border-4 border-opacity-40" src="https://ui.glass/generator/static/profile-picture-3-b701fcb37cb1fef6a7e720dccd16e4c0.jpg" alt="" >
          <div class="card-name-user text-xs">
            <h3 class="font-semibold">Jeny Green</h3>
            <div class=" flex items-center gap-x-1">
              <span class="h-3 w-3 rounded-full bg-red-500"></span>
              <span>Offline</span>
            </div>
          </div>
        </div>

        <div class="card-action">
           <button class="flex items-center px-2 py-1 text-xs text-white bg-green-500 hover:bg-green-600">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
            <span class="">Invite</span>
          </button>
        </div>
      </div>

      <div class="card-content-profil pt-3 flex justify-between items-center">
        <div class=" flex gap-x-2 items-center">
          <img class="avatar h-10 w-10 rounded-full border-4 border-opacity-40" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAASABIAAD/4QCuRXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgExAAIAAAAhAAAAWodpAAQAAAABAAAAfAAAAAAAAABIAAAAAQAAAEgAAAABQWRvYmUgUGhvdG9zaG9wIDIxLjAgKE1hY2ludG9zaCkAAAADoAEAAwAAAAEAAQAAoAIABAAAAAEAAABAoAMABAAAAAEAAABAAAAAAP/hC0NodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDYuMC4wIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RDNFMzkyREQ2MkY2MTFFQkJBQUI4RThDNTFDQzgyODgiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RDNFMzkyREM2MkY2MTFFQkJBQUI4RThDNTFDQzgyODgiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3NTAxMDgwNDEyMTAxMUVBOTNGNUU1NkMyNEY0RUY2MCIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjEuMCAoTWFjaW50b3NoKSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkQzODcxMkEwNTRFNTExRUJBOTVBQTQzQzdBMTExOUFDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkQzODcxMkExNTRFNTExRUJBOTVBQTQzQzdBMTExOUFDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDw/eHBhY2tldCBlbmQ9InciPz4A/+0AOFBob3Rvc2hvcCAzLjAAOEJJTQQEAAAAAAAAOEJJTQQlAAAAAAAQ1B2M2Y8AsgTpgAmY7PhCfv/AABEIAEAAQAMBEQACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2wBDAAYEBAQFBAYFBQYJBgUGCQsIBgYICwwKCgsKCgwQDAwMDAwMEAwODxAPDgwTExQUExMcGxsbHB8fHx8fHx8fHx//2wBDAQcHBw0MDRgQEBgaFREVGh8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx//3QAEAAj/2gAMAwEAAhEDEQA/ANiFuleazyUXojUM0iR654l0nw/pxvtSmEceQkaD78jnoqj9SegHJ4pRg5OyOyGx58vxk1S/vhFpsaKgJ3Rou8gdtzPhj+CgV0fVUlqXzu5sRfE7X9JuYv7VtUv9OkYB7iJGgnjBHZTmOXn3WspUItaOzN0pLdaHp2iazpusafFqGnTCe1mHyuOCCDhlZTyrKeCDyDXFOLi7M2ijUQVFzRRJRSLUT//Q1IWrzWeSi/CckVDNYnjviy4bxN4klkl3PbW8ptLO3HGEjOGP1kcEnHYCumn7sbn6DlWQUp4dVKt+9vkeweANPsdNtoDFZR2hIURkRYyR1G7nn8a4pOTfcivSprSKSS7Hp882lzgWt2YHd+RDJsJJHcAjP41TV0eUlbY5LU9Og0HXYJLGFIbDVHK3MaDbtmI+WTA4IY4BrGcSKiTNZGrAhIlU0GiR/9G9A9eczyUX4n4/z6VDNYbnicMapayTTMwSWeTnByT5jDHHPUc11dD9fwvKsCuq00/Cx2HgzWdb0TX9Hs0I/sfWLnydqFn2MuQSVflSrY9iOlZVKel+p8vQxMKs5RUbNX6Ws1+a0eqPZ77UNTsfEkVlEpU3A+SRPLIcEHLOHG7aCMHHTNRBX62OKtUtFNQc9baW91d90XfFFrqN9oVtLBCF1GOeJkiBCg5bDjk4AK+9YvUcoq9lsNRxnggg9CCCD9CODXI1Yy5WnZ7lhGqGaJH/0p4H6V57PJRal+0PaTLbtsuGjcQvxw5U7TzkdahnZgpQjWi5q8U1deR5lFHDBCpvIN62106zW8nqQGfPvuz+NdK1vY/aqdGE6coQ92O8beiat5difVdc0a017TPsYYW9sUuW6swKuCFH5HisoRbiz53DThGpOL+Nxev4fLzZ9DyeL7FrC21SW1kGmM8am7YK3lmYALJwSwTedrEgbTyeMms3E8FUr6XXMbxnW5iVon8vDBlYgEDYd3IPGCAQazlv2Eo8u+pzzyxmZzGMRlmKj2JJ/rXLJ3ZzSqc0rv8Aq2hNHJWTLiz/0yB64GeSjSt36VmzopIwPG+jRy6c9/CuJUdWnA6Fcbd2PUZGT6VVKVnY+94Yzed/q837tnyd772v27LoedSJNa6tFIlpJd5aNY1iCF+CSn3/AJeSO9bU9U0KrinQ5/dvKTSv2Sv+Z6zpfjDxZqxt9EfQnTR7hri01OW6mjkkXbbySH5IkVVwQvO49cY701TUU7njxq1JSvpqejvcMNBtgxIkkEYPb7sYLfqa4KxeIdlbuynG5xXMzliTpKRUs3iz/9SGB+9cTPIRpW74FZM66SLZCTQvC4DJIpVlPcEYNQ0duHqOE4yXRp/ieUpNeW+qQixQXF5CMJCer7eSuMjJ3LkYOcjiui6WvQ/SMbTgpydrqS1X5M9q8C3t/qVlc3V9pQ02a4GZpS2eq4Y4JyAQBngZ71FSaastWz5mcFGzeiXQ2Nf1GwjGnReckQlSTyEdgpfaRkqD16isKlN9Fex5uKqpSV2k3crxycAg1ytExZMr1DNon//Vo271xtHjxZbudUsdOtDc3s6wQLgF3Pc8ADuST0ArPlbeh3UloeZeK/iDqV9qv2G1nkstJjdfMMRMc0qggsWcYZRj+EYPqe1dVOglG71Z34aEXWjGWkbpy9L3a+4BY3mqX6vYnc/30YE5Ofm4I5z3rKbSP0TN5QcoTg00uq7P/gHuHwx0y4h0lrjVbqW8nkUGLzmJCL0C47nPc81hKemisfMYpp1Hba5L8Z9BtNS8JG5FwlpfaK32qyeRgqStja0Bz18xTgY6Ng+1KjWanoefisNGtTakeX+HfFWqR2MN3YXLeQQA8T/Mn4ofun2BFexPDU6i95a/ifA/Xa2Fm4xbsuj1Xl/SZ33hvxrb6pJ9muFEF5xtx9x/Zc9D7V5GLwDp6x1j+KPpMszhV/dnaM+nZ+nn5fcf/9bEN5FbQNNKwCIM8kDJ9Bnua5VG7PJpR5pJdzzvxtqV5d6jD5jExfu5Ioj90fMVOB0711wgkjscuWpy9FYytRs9+pqU5Dpk49Rj/GqmuWKNMFP2laVujf8Aka3h9NW0m9jurG7a2lU7h8odD6gowYVyzaluj6OFJwVlJpPddPu6fI7GPxz4vWMRR3sUAJyWihUHOc8biwHPtWfso9g5Xfcbc3d7qTefql7NqEyr8rztnGRzhRhVyD/CBTSS2VjSNNHOaNDHpk0toHJWctLCB90qGO09T2IBH416tOLS1PzTM5RqycofCm1+P9NG7bFVkWUN5cpwwAPIYHI57c1py3PI55R26dT/2Q==" alt="" >
          <div class="card-name-user text-xs">
            <h3 class="font-semibold">Neil Sims</h3>
            <div class=" flex items-center gap-x-1">
              <span class="h-3 w-3 rounded-full bg-green-500"></span>
              <span>Online</span>
            </div>
          </div>
        </div>

        <div class="card-action">
          <button class="flex items-center px-2 py-1 text-xs text-white bg-green-500 hover:bg-green-600">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
            <span class="">Invite</span>
          </button>
        </div>
      </div>
    </div>

  </div>

<!-- BUY ME A BEER AND HELP SUPPORT OPEN-SOURCE RESOURCES -->
<div class="flex items-end justify-end fixed bottom-0 right-0 mb-4 mr-4 z-10">
    <div>
        <a title="Buy me a beer" href="https://www.buymeacoffee.com/emichel" target="_blank" class="block w-16 h-16 rounded-full transition-all shadow hover:shadow-lg transform hover:scale-110 hover:rotate-12">
            <img class="object-cover object-center w-full h-full rounded-full" src="https://i.pinimg.com/originals/60/fd/e8/60fde811b6be57094e0abc69d9c2622a.jpg"/>
        </a>
    </div>
</div>
</div>''', '''<!-- component -->
<div class="h-screen flex bg-gray-900 items-center justify-center">
  <div class="grid grid-cols-12 gap-2 gap-y-4 max-w-6xl">
    
    <!-- Video 1 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/59/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">

          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/1/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>

        </div>
      </card>
    </div>

    <!-- Video 2 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/60/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">

          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/4/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>

        </div>
      </card>
    </div>

    <!-- Video 3 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/22/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">
          
          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/88/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>

        </div>
      </card>
    </div>

    <!-- Video 4 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/90/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">
          
          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/57/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>
          
        </div>
      </card>
    </div>
  </div>
</div>''', '''<!-- component -->
<div class="font-sans antialiased h-screen flex">
    <!-- Sidebar / channel list -->
    <div class="bg-indigo-darkest text-purple-lighter flex-none w-24 p-6 hidden md:block">
        <div class="cursor-pointer mb-4">
            <div class="bg-white h-12 w-12 flex items-center justify-center text-black text-2xl font-semibold rounded-lg mb-1 overflow-hidden">
                <img src="https://pbs.twimg.com/profile_images/895274026783866881/E1G1nNb0_400x400.jpg" alt="">
            </div>
            <div class="text-center text-white opacity-50 text-sm">&#8984;1</div>
        </div>
        <div class="cursor-pointer mb-4">
            <div class="bg-indigo-lighter opacity-25 h-12 w-12 flex items-center justify-center text-black text-2xl font-semibold rounded-lg mb-1 overflow-hidden">
                L
            </div>
            <div class="text-center text-white opacity-50 text-sm">&#8984;2</div>
        </div>
        <div class="cursor-pointer">
            <div class="bg-white opacity-25 h-12 w-12 flex items-center justify-center text-black text-2xl font-semibold rounded-lg mb-1 overflow-hidden">
                <svg class="fill-current h-10 w-10 block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M16 10c0 .553-.048 1-.601 1H11v4.399c0 .552-.447.601-1 .601-.553 0-1-.049-1-.601V11H4.601C4.049 11 4 10.553 4 10c0-.553.049-1 .601-1H9V4.601C9 4.048 9.447 4 10 4c.553 0 1 .048 1 .601V9h4.399c.553 0 .601.447.601 1z"/></svg>
            </div>
        </div>
      
      
      
    </div>
    <div class="bg-indigo-darker text-purple-lighter flex-none w-64 pb-6 hidden md:block">
        <div class="text-white mb-2 mt-3 px-4 flex justify-between">
            <div class="flex-auto">
                <h1 class="font-semibold text-xl leading-tight mb-1 truncate">Tailwind CSS</h1>
                <div class="flex items-center mb-6">
                    <span class="bg-green rounded-full block w-2 h-2 mr-2"></span>
                    <span class="text-white opacity-50 text-sm">Adam Wathan</span>
                </div>
            </div>
            <div>
                <svg class="h-6 w-6 fill-current text-white opacity-25" viewBox="0 0 20 20">
                    <path d="M14 8a4 4 0 1 0-8 0v7h8V8zM8.027 2.332A6.003 6.003 0 0 0 4 8v6l-3 2v1h18v-1l-3-2V8a6.003 6.003 0 0 0-4.027-5.668 2 2 0 1 0-3.945 0zM12 18a2 2 0 1 1-4 0h4z" fill-rule="evenodd" />
                </svg>
            </div>
        </div>
        <div class="mb-8">
            <div class="px-4 mb-2 text-white flex justify-between items-center">
                <div class="opacity-75">Channels</div>
                <div>
                    <svg class="fill-current h-4 w-4 opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M11 9h4v2h-4v4H9v-4H5V9h4V5h2v4zm-1 11a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z" />
                    </svg>
                </div>
            </div>
            <div class="bg-teal-dark py-1 px-4 text-white"># general</div>
        </div>
        <div class="mb-8">
            <div class="px-4 mb-2 text-white flex justify-between items-center">
                <div class="opacity-75">Direct Messages</div>
                <div>
                    <svg class="fill-current h-4 w-4 opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M11 9h4v2h-4v4H9v-4H5V9h4V5h2v4zm-1 11a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z" />
                    </svg>
                </div>
            </div>
            <div class="flex items-center mb-3 px-4">
                <span class="bg-green rounded-full block w-2 h-2 mr-2"></span>
                <span class="text-white opacity-75">Adam Wathan <span class="text-grey text-sm">(you)</span></span>
            </div>
            <div class="flex items-center mb-3 px-4">
                <span class="bg-green rounded-full block w-2 h-2 mr-2"></span>
                <span class="text-white opacity-75">David Hemphill</span>
            </div>
            <div class="flex items-center px-4 mb-6 opacity-50">
                <span class="border border-white rounded-full w-2 h-2 mr-2"></span>
                <span class="text-white">Steve Schoger</span>
            </div>
        </div>
        <div>
            <div class="px-4 mb-2 text-white flex justify-between items-center">
                <div class="opacity-75">Apps</div>
                <div>
                    <svg class="fill-current h-4 w-4 opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M11 9h4v2h-4v4H9v-4H5V9h4V5h2v4zm-1 11a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z" />
                    </svg>
                </div>
            </div>
        </div>
    </div>
    <!-- Chat content -->
    <div class="flex-1 flex flex-col bg-white overflow-hidden">
        <!-- Top bar -->
        <div class="border-b flex px-6 py-2 items-center flex-none">
            <div class="flex flex-col">
                <h3 class="text-grey-darkest mb-1 font-extrabold">#general</h3>
                <div class="text-grey-dark text-sm truncate">
                    Chit-chattin' about ugly HTML and mixing of concerns.
                </div>
            </div>
            <div class="ml-auto hidden md:block">
                <div class="relative">
                    <input type="search" placeholder="Search" class="appearance-none border border-grey rounded-lg pl-8 pr-4 py-2">
                    <div class="absolute pin-y pin-l pl-3 flex items-center justify-center">
                        <svg class="fill-current text-grey h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                            <path d="M12.9 14.32a8 8 0 1 1 1.41-1.41l5.35 5.33-1.42 1.42-5.33-5.34zM8 14A6 6 0 1 0 8 2a6 6 0 0 0 0 12z" />
                        </svg>
                    </div>
                </div>
            </div>
        </div>
        <!-- Chat messages -->
        <div class="px-6 py-4 flex-1 overflow-y-scroll">
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/875010472105222144/Pkt9zqPY_400x400.jpg" class="w-10 h-10 rounded mr-3">
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Steve Schoger</span>
                        <span class="text-grey text-xs">11:46</span>
                    </div>
                    <p class="text-black leading-normal">The slack from the other side.</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/887661330832003072/Zp6rA_e2_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Adam Wathan</span>
                        <span class="text-grey text-xs">12:45</span>
                    </div>
                    <p class="text-black leading-normal">How are we supposed to control the marquee space without an utility for it? I propose this:</p>
                    <div class="bg-grey-lighter border border-grey-light text-grey-darkest text-sm font-mono rounded p-3 mt-2 whitespace-pre overflow-scroll">.marquee-lightspeed { -webkit-marquee-speed: fast; }
.marquee-lightspeeder { -webkit-marquee-speed: faster; }</div>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/929910740156215296/yDEC9GW9_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">David Hemphill</span>
                        <span class="text-grey text-xs">12:46</span>
                    </div>
                    <p class="text-black leading-normal"><a href="#" class="inline-block bg-blue-lightest text-blue no-underline">@Adam Wathan</a> the size of the generated CSS is creating a singularity in space/time, we must stop adding more utilities before it's too late!</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/875010472105222144/Pkt9zqPY_400x400.jpg" class="w-10 h-10 rounded mr-3">
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Steve Schoger</span>
                        <span class="text-grey text-xs">11:46</span>
                    </div>
                    <p class="text-black leading-normal">The slack from the other side.</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/887661330832003072/Zp6rA_e2_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Adam Wathan</span>
                        <span class="text-grey text-xs">12:45</span>
                    </div>
                    <p class="text-black leading-normal">How are we supposed to control the marquee space without an utility for it? I propose this:</p>
                    <div class="bg-grey-lighter border border-grey-light text-grey-darkest text-sm font-mono rounded p-3 mt-2 whitespace-pre overflow-scroll">.marquee-lightspeed { -webkit-marquee-speed: fast; }
.marquee-lightspeeder { -webkit-marquee-speed: faster; }</div>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/929910740156215296/yDEC9GW9_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">David Hemphill</span>
                        <span class="text-grey text-xs">12:46</span>
                    </div>
                    <p class="text-black leading-normal"><a href="#" class="inline-block bg-blue-lightest text-blue no-underline">@Adam Wathan</a> the size of the generated CSS is creating a singularity in space/time, we must stop adding more utilities before it's too late!</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/875010472105222144/Pkt9zqPY_400x400.jpg" class="w-10 h-10 rounded mr-3">
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Steve Schoger</span>
                        <span class="text-grey text-xs">11:46</span>
                    </div>
                    <p class="text-black leading-normal">The slack from the other side.</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/887661330832003072/Zp6rA_e2_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Adam Wathan</span>
                        <span class="text-grey text-xs">12:45</span>
                    </div>
                    <p class="text-black leading-normal">How are we supposed to control the marquee space without an utility for it? I propose this:</p>
                    <div class="bg-grey-lighter border border-grey-light text-grey-darkest text-sm font-mono rounded p-3 mt-2 whitespace-pre overflow-scroll">.marquee-lightspeed { -webkit-marquee-speed: fast; }
.marquee-lightspeeder { -webkit-marquee-speed: faster; }</div>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/929910740156215296/yDEC9GW9_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">David Hemphill</span>
                        <span class="text-grey text-xs">12:46</span>
                    </div>
                    <p class="text-black leading-normal"><a href="#" class="inline-block bg-blue-lightest text-blue no-underline">@Adam Wathan</a> the size of the generated CSS is creating a singularity in space/time, we must stop adding more utilities before it's too late!</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/875010472105222144/Pkt9zqPY_400x400.jpg" class="w-10 h-10 rounded mr-3">
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Steve Schoger</span>
                        <span class="text-grey text-xs">11:46</span>
                    </div>
                    <p class="text-black leading-normal">The slack from the other side.</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/887661330832003072/Zp6rA_e2_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Adam Wathan</span>
                        <span class="text-grey text-xs">12:45</span>
                    </div>
                    <p class="text-black leading-normal">How are we supposed to control the marquee space without an utility for it? I propose this:</p>
                    <div class="bg-grey-lighter border border-grey-light text-grey-darkest text-sm font-mono rounded p-3 mt-2 whitespace-pre overflow-scroll">.marquee-lightspeed { -webkit-marquee-speed: fast; }
.marquee-lightspeeder { -webkit-marquee-speed: faster; }</div>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/929910740156215296/yDEC9GW9_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">David Hemphill</span>
                        <span class="text-grey text-xs">12:46</span>
                    </div>
                    <p class="text-black leading-normal"><a href="#" class="inline-block bg-blue-lightest text-blue no-underline">@Adam Wathan</a> the size of the generated CSS is creating a singularity in space/time, we must stop adding more utilities before it's too late!</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/875010472105222144/Pkt9zqPY_400x400.jpg" class="w-10 h-10 rounded mr-3">
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Steve Schoger</span>
                        <span class="text-grey text-xs">11:46</span>
                    </div>
                    <p class="text-black leading-normal">The slack from the other side.</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/887661330832003072/Zp6rA_e2_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Adam Wathan</span>
                        <span class="text-grey text-xs">12:45</span>
                    </div>
                    <p class="text-black leading-normal">How are we supposed to control the marquee space without an utility for it? I propose this:</p>
                    <div class="bg-grey-lighter border border-grey-light text-grey-darkest text-sm font-mono rounded p-3 mt-2 whitespace-pre overflow-scroll">.marquee-lightspeed { -webkit-marquee-speed: fast; }
.marquee-lightspeeder { -webkit-marquee-speed: faster; }</div>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/929910740156215296/yDEC9GW9_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">David Hemphill</span>
                        <span class="text-grey text-xs">12:46</span>
                    </div>
                    <p class="text-black leading-normal"><a href="#" class="inline-block bg-blue-lightest text-blue no-underline">@Adam Wathan</a> the size of the generated CSS is creating a singularity in space/time, we must stop adding more utilities before it's too late!</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/875010472105222144/Pkt9zqPY_400x400.jpg" class="w-10 h-10 rounded mr-3">
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Steve Schoger</span>
                        <span class="text-grey text-xs">11:46</span>
                    </div>
                    <p class="text-black leading-normal">The slack from the other side.</p>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/887661330832003072/Zp6rA_e2_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">Adam Wathan</span>
                        <span class="text-grey text-xs">12:45</span>
                    </div>
                    <p class="text-black leading-normal">How are we supposed to control the marquee space without an utility for it? I propose this:</p>
                    <div class="bg-grey-lighter border border-grey-light text-grey-darkest text-sm font-mono rounded p-3 mt-2 whitespace-pre overflow-scroll">.marquee-lightspeed { -webkit-marquee-speed: fast; }
.marquee-lightspeeder { -webkit-marquee-speed: faster; }</div>
                </div>
            </div>
            <!-- A message -->
            <div class="flex items-start mb-4 text-sm">
                <img src="https://pbs.twimg.com/profile_images/929910740156215296/yDEC9GW9_400x400.jpg" class="w-10 h-10 rounded mr-3" />
                <div class="flex-1 overflow-hidden">
                    <div>
                        <span class="font-bold">David Hemphill</span>
                        <span class="text-grey text-xs">12:46</span>
                    </div>
                    <p class="text-black leading-normal"><a href="#" class="inline-block bg-blue-lightest text-blue no-underline">@Adam Wathan</a> the size of the generated CSS is creating a singularity in space/time, we must stop adding more utilities before it's too late!</p>
                </div>
            </div>
        </div>
        <div class="pb-6 px-4 flex-none">
            <div class="flex rounded-lg border-2 border-grey overflow-hidden">
                <span class="text-3xl text-grey border-r-2 border-grey p-2">
                    <svg class="fill-current h-6 w-6 block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M16 10c0 .553-.048 1-.601 1H11v4.399c0 .552-.447.601-1 .601-.553 0-1-.049-1-.601V11H4.601C4.049 11 4 10.553 4 10c0-.553.049-1 .601-1H9V4.601C9 4.048 9.447 4 10 4c.553 0 1 .048 1 .601V9h4.399c.553 0 .601.447.601 1z"/></svg>
                  </span>
                <input type="text" class="w-full px-4" placeholder="Message #general" />
            </div>
        </div>
    </div>
</div>''', '''<!-- component -->
<body class = "body bg-white dark:bg-[#0F172A]">
    <div class = "bg-black before:animate-pulse before:bg-gradient-to-b before:from-gray-900 overflow-hidden before:via-[#00FF00] before:to-gray-900 before:absolute ">
        <div id="myDIV" >
            <div class = "w-[100vw] h-[100vh] px-3 sm:px-5 flex items-center justify-center absolute">
                <div class = "w-full sm:w-1/2 lg:2/3 px-6 bg-gray-500 bg-opacity-20 bg-clip-padding backdrop-filter backdrop-blur-sm text-white z-50 py-4  rounded-lg">
                    <div class = "w-full flex justify-center text-[#00FF00] text-xl mb:2 md:mb-5">
                        Sign In
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-xs font-medium text-white">Your email</label>
                        <input type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5 md:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@neurolink.com" required>
                    </div>
                    <div class="mb-6">
                        <label for="password" class="block mb-2 text-xs font-medium text-white">Your password</label>
                        <input type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5 md:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                    </div>
                    <div class = "flex flex-row justify-between">
                        <div class = "text-white text-sm md:text-md ">Forgot Password</div>
                        <div class = "text-[#00FF00] text-sm md:text-md">Signup</div>
                    </div>
                    <div class = "mt-4 md:mt-10 w-full flex justify-center text-sm md:text-xl bg-[#00FF00] py-2 rounded-md">
                        Login
                    </div>
        
                </div>
            </div>
        </div>
    </div>
</body>
    
    
    <script>
        const para = document.createElement("div");
        para.className = 'flex flex-wrap gap-0.5 h-screen items-center justify-center  relative';
            let el = '<div class = "  transition-colors duration-[1.5s] hover:duration-[0s] border-[#00FF00] h-[calc(5vw-2px)] w-[calc(5vw-2px)] md:h-[calc(4vw-2px)] md:w-[calc(4vw-2px)] lg:h-[calc(3vw-4px)] lg:w-[calc(3vw-4px)] bg-gray-900 hover:bg-[#00FF00]"></div>'
            for (var k = 1; k<=1000; k++){
                el+= '<div class = " transition-colors duration-[1.5s] hover:duration-[0s] border-[#00FF00] h-[calc(5vw-2px)] w-[calc(5vw-2px)] md:h-[calc(4vw-2px)] md:w-[calc(4vw-2px)] lg:h-[calc(3vw-4px)] lg:w-[calc(3vw-4px)] bg-gray-900 hover:bg-[#00FF00]"></div>';
            };
    
            para.innerHTML = el;
        document.getElementById("myDIV").appendChild(para);
    </script>''', '''<!-- component -->
<div class="bg-green-200 py-32 px-10 min-h-screen ">
  <!--   tip; mx-auto -- jagab ilusti keskele  -->
  <div class="bg-white p-10 md:w-3/4 lg:w-1/2 mx-auto">

    <form action="">

      <!--       flex - asjad korvuti, nb! flex-1 - element kogu ylejaanud laius -->
      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="name" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Text</label>
        <input type="text" id="name" name="name" placeholder="Name" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Number</label>
        <input type="number" id="number" name="number" placeholder="number" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Range</label>
        <input type="range" id="range" name="range" placeholder="range" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">File</label>
        <input type="file" id="file" name="file" placeholder="file" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Date</label>
        <input type="date" id="date" name="date" placeholder="date" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Month</label>
        <input type="month" id="month" name="month" placeholder="month" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Time</label>
        <input type="time" id="time" name="time" placeholder="time" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Password</label>
        <input type="password" id="password" name="password" placeholder="password" 
               class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
      </div>

      <div class="flex items-center mb-5">
        <!--         tip - here neede inline-block , but why? -->
        <label for="number" class="inline-block w-20 mr-6 text-right 
                                 font-bold text-gray-600">Select</label>
        <select class="flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 
                      text-gray-600 placeholder-gray-400
                      outline-none">
            <option>Surabaya</option>
            <option>Jakarta</option>
            <option>bandung</option>
            <option>Tangerang</option>
        </select>
      </div>

      <div class="text-right">
        <button class="py-3 px-8 bg-green-400 text-white font-bold">Submit</button> 
      </div>

    </form>
  </div>
</div>''', '''<!-- component -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
</head>
<style>
    #nav-mobile-btn.close span:first-child{
        transform: rotate(45deg);
        top: 4px;
        position: relative;
        background:#a0aec0;
    }
    #nav-mobile-btn.close span:nth-child(2){
        transform: rotate(-45deg);
        margin-top: 0px;
        background:#a0aec0;
    }
    html {
            scroll-behavior: smooth;
            background: #ffffff !important;
        }
</style>
<body class="overflow-x-hidden antialiased w-full">

    <!-- HERO SECTION -->
    <div>
        <div class="z-30 relative items-center justify-center w-full w-screen h-screen">
            <div>
                <div class="inset-0  h-screen">
                    <!-- <video 
                        src="https://youtu.be/OhyQRljsp2w" 
                        autoplay 
                        muted 
                        loop 
                        class="object-cover w-full h-full"
                    >
                    </video>      -->
                    <iframe class="object-cover w-full h-full" src="https://www.youtube.com/embed/OhyQRljsp2w?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>

                <div class="absolute inset-0 z-40  flex justify-between h-full px-8 " >
                    <div class="relative z-20 w-full h-24  pt-2 ">
                        <div class="flex items-center justify-between h-full w-full">
                            <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F4.bp.blogspot.com%2F-Vwuv72HQYhs%2FVW6yjk1BqEI%2FAAAAAAAAC5Y%2FuDFxGmthr9A%2Fs1600%2FVans-vector-logo.png&f=1&nofb=1" class="w-auto h-12"/>

                            <div id="nav" class=" text-white absolute top-0 left-0 hidden block w-full mt-20 border-b border-gray-200 sm:border-none sm:px-5 sm:block sm:relative sm:mt-0 sm:px-0 sm:w-auto">
                                <nav class="flex flex-col items-center py-3  bg-red-500 sm:flex-row sm:bg-transparent sm:border-none sm:py-0">
                                    <a href="#" class="px-1 mb-1 mb-5 mr-0 text-base sm:mb-0 sm:mr-4 lg:mr-8">About</a>
                                    <a href="#_" class="px-1 mb-1 mb-5 mr-0 text-base sm:mb-0 sm:mr-4 lg:mr-8">Contact</a>
                                    <a href="#" class="px-1 mb-1 mb-5 mr-0 text-base sm:mb-0 sm:mr-4 lg:mr-8">Servies & Products</a>
                                </nav>
                            </div>

                            <div id="nav-mobile-btn" class="absolute top-0 right-0 z-50 block w-6 mt-8 mr-10 cursor-pointer select-none sm:hidden sm:mt-10">
                                <span class="block w-full h-1 mt-2 duration-200 transform bg-white rounded-full sm:mt-1"></span>
                                <span class="block w-full h-1 mt-1 duration-200 transform bg-white rounded-full"></span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="absolute inset-0 z-20 flex items-center justify-center h-screen w-full bg-gray-900 bg-opacity-50"></div>
                <div data-aos="flip-down" class="absolute inset-0  z-30 container flex flex-col items-center justify-center h-full max-w-6xl pl-0 mx-auto  sm:pl-8 xl:pl-0 md:flex-row md:justify-between">
                    <div class="flex flex-col items-center justify-center mx-auto">
                        <div class="relative text-center ">
                            <h1 class="text-white relative mb-4 text-6xl font-bold font-sans italic leading-none text-center lg:text-9xl xl:text-9xl"> MY HERO<br><span class="text-red-500">SECTION</span></h1>
                            <p class="text-gray-400 text-sm lg:text-4xl lg:text-center font-sans italic">Semoga Bermanfaat Untuk Semua
                            </p>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- HERO SECTION END -->


<script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script>
        AOS.init({
            offset:100,
            duration :1000
        });
    </script>
    <script>
        if( document.getElementById('nav-mobile-btn') ){
            document.getElementById('nav-mobile-btn').addEventListener('click', function(){
                if( this.classList.contains('close') ){
                    document.getElementById('nav').classList.add('hidden');
                    this.classList.remove('close');
                } else {
                    document.getElementById('nav').classList.remove('hidden');
                    this.classList.add('close');
                }
            });
        }
    </script>
</body>
</html>''', '''<!-- component -->
<!-- This is an example component -->
<div class="h-screen font-sans login bg-cover">
<div class="container mx-auto h-full flex flex-1 justify-center items-center">
    <div class="w-full max-w-lg">
      <div class="leading-loose">
        <form class="max-w-sm m-4 p-10 bg-white bg-opacity-25 rounded shadow-xl">
            <p class="text-white font-medium text-center text-lg font-bold">LOGIN</p>
              <div class="">
                <label class="block text-sm text-white" for="email">E-mail</label>
                <input class="w-full px-5 py-1 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white" type="email" id="email"  placeholder="Digite o e-mail" aria-label="email" required>
              </div>
              <div class="mt-2">
                <label class="block  text-sm text-white">Senha</label>
                 <input class="w-full px-5 py-1 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white"
                  type="password" id="password" placeholder="Digite a sua senha" arial-label="password" required>
              </div>

              <div class="mt-4 items-center flex justify-between">
                <button class="px-4 py-1 text-white font-light tracking-wider bg-gray-900 hover:bg-gray-800 rounded"
                  type="submit">Entrar</button>
                <a class="inline-block right-0 align-baseline font-bold text-sm text-500 text-white hover:text-red-400"
                  href="#">Esqueceu a senha ?</a>
              </div>
              <div class="text-center">
                <a class="inline-block right-0 align-baseline font-light text-sm text-500 hover:text-red-400">
                    Criar uma conta
                </a>
              </div>

        </form>

      </div>
    </div>
  </div>
</div>
<style>
  .login{
  /*
    background: url('https://tailwindadmin.netlify.app/dist/images/login-new.jpeg');
  */
  background: url('http://bit.ly/2gPLxZ4');
  background-repeat: no-repeat;
  background-size: cover;
}
</style>''', '''<!-- component -->
<div class="flex h-screen w-full items-center justify-center bg-gray-900 bg-cover bg-no-repeat" style="background-image:url('https://images.unsplash.com/photo-1499123785106-343e69e68db1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1748&q=80')">
  <div class="rounded-xl bg-gray-800 bg-opacity-50 px-16 py-10 shadow-lg backdrop-blur-md max-sm:px-8">
    <div class="text-white">
      <div class="mb-8 flex flex-col items-center">
        <img src="https://www.logo.wine/a/logo/Instagram/Instagram-Glyph-Color-Logo.wine.svg" width="150" alt="" srcset="" />
        <h1 class="mb-2 text-2xl">Instagram</h1>
        <span class="text-gray-300">Enter Login Details</span>
      </div>
      <form action="#">
        <div class="mb-4 text-lg">
          <input class="rounded-3xl border-none bg-yellow-400 bg-opacity-50 px-6 py-2 text-center text-inherit placeholder-slate-200 shadow-lg outline-none backdrop-blur-md" type="text" name="name" placeholder="id@email.com" />
        </div>

        <div class="mb-4 text-lg">
          <input class="rounded-3xl border-none bg-yellow-400 bg-opacity-50 px-6 py-2 text-center text-inherit placeholder-slate-200 shadow-lg outline-none backdrop-blur-md" type="Password" name="name" placeholder="*********" />
        </div>
        <div class="mt-8 flex justify-center text-lg text-black">
          <button type="submit" class="rounded-3xl bg-yellow-400 bg-opacity-50 px-10 py-2 text-white shadow-xl backdrop-blur-md transition-colors duration-300 hover:bg-yellow-600">Login</button>
        </div>
      </form>
    </div>
  </div>
</div>''', '''<!-- component -->
<section id="contact" class="relative w-full min-h-screen bg-black text-red-500">
<h1 class="text-4xl p-4 font-bold tracking-wide">
    Contact
</h1>
<div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-red-800 h-32 w-full"></div>

<!-- wrapper -->
<div class="relative p-5 lg:px-20 flex flex-col md:flex-row items-center justify-center">

    <!-- Social Media -->
    <div class="w-full md:w-1/2 p-5 md:px-0 mx-5">
    <div class="bg-gray-900 border border-red-500 w-full lg:w-1/2 h-full p-5 pt-8">
        <h3 class="text-2xl font-semibold mb-5">
        My Social Media
        </h3>
        <!-- list -->
        <div class="flex flex-col gap-3">
        <a href="#" class="flex items-center hover:text-white hover:bg-red-500 p-2">
            <svg fill="currentColor" class="w-6 h-6 m-2" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            Github
        </a>
        <a href="#" class="flex items-center hover:text-white hover:bg-red-500 p-2">
            <svg fill="currentColor" class="w-6 h-6 m-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" >
            <path d="M 21.800781 0 L 2.199219 0 C 1 0 0 1 0 2.199219 L 0 21.800781 C 0 23 1 24 2.199219 24 L 21.800781 24 C 23 24 24 23 24 21.800781 L 24 2.199219 C 24 1 23 0 21.800781 0 Z M 7 20 L 3 20 L 3 9 L 7 9 Z M 5 7.699219 C 3.800781 7.699219 3 6.898438 3 5.898438 C 3 4.800781 3.800781 4 5 4 C 6.199219 4 7 4.800781 7 5.800781 C 7 6.898438 6.199219 7.699219 5 7.699219 Z M 21 20 L 17 20 L 17 14 C 17 12.398438 15.898438 12 15.601563 12 C 15.300781 12 14 12.199219 14 14 C 14 14.199219 14 20 14 20 L 10 20 L 10 9 L 14 9 L 14 10.601563 C 14.601563 9.699219 15.601563 9 17.5 9 C 19.398438 9 21 10.5 21 14 Z"/>
            </svg>
            Linkedin
        </a>
        <a href="#" class="flex items-center hover:text-white hover:bg-red-500 p-2">
            <svg fill="currentColor" class="w-6 h-6 m-2" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" >
            <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
            </svg>
            Youtube
        </a>
        <a href="#" class="flex items-center hover:text-white hover:bg-red-500 p-2">
            <svg fill="currentColor" class="w-6 h-6 m-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" >
            <path d="M12,0C5.373,0,0,5.373,0,12c0,6.016,4.432,10.984,10.206,11.852V15.18H7.237v-3.154h2.969V9.927c0-3.475,1.693-5,4.581-5 c1.383,0,2.115,0.103,2.461,0.149v2.753h-1.97c-1.226,0-1.654,1.163-1.654,2.473v1.724h3.593L16.73,15.18h-3.106v8.697 C19.481,23.083,24,18.075,24,12C24,5.373,18.627,0,12,0z"/>
            </svg>
            Facebook
        </a>
        </div>
    </div>
    </div>

    <!-- Contact Me -->
    <form action="#" class="w-full md:w-1/2 border border-red-500 p-6 bg-gray-900">
    <h2 class="text-2xl pb-3 font-semibold">
        Send Message
    </h2>
    <div>
        <div class="flex flex-col mb-3">
        <label for="name">Name</label>
        <input 
            type="text" id="name" 
            class="px-3 py-2 bg-gray-800 border border-gray-900 focus:border-red-500 focus:outline-none focus:bg-gray-800 focus:text-red-500"
            autocomplete="off"
        >
        </div>
        <div class="flex flex-col mb-3">
        <label for="email">Email</label>
        <input 
            type="text" id="email" 
            class="px-3 py-2 bg-gray-800 border border-gray-900 focus:border-red-500 focus:outline-none focus:bg-gray-800 focus:text-red-500"
            autocomplete="off"
        >
        </div>
        <div class="flex flex-col mb-3">
        <label for="message">Message</label>
        <textarea 
            rows="4" id="message" 
            class="px-3 py-2 bg-gray-800 border border-gray-900 focus:border-red-500 focus:outline-none focus:bg-gray-800 focus:text-red-500"
        ></textarea>
        </div>
    </div>
    <div class="w-full pt-3">
        <button type="submit" class="w-full bg-gray-900 border border-red-500 px-4 py-2 transition duration-50 focus:outline-none font-semibold hover:bg-red-500 hover:text-white text-xl cursor-pointer">
        Send
        </button>
    </div>
    </form>
</div>
</section>''', '''<!-- component -->
<div class="mx-auto container px-6 xl:px-0 py-12">
  <!--- more free and premium Tailwind CSS components at https://tailwinduikit.com/ --->

  <div class="flex flex-col">
    <div class="flex flex-col justify-center">
      <div class="relative">
        <img class="hidden sm:block w-full" src="https://i.ibb.co/HxXSY0j/jason-wang-Nx-Awry-Abt-Iw-unsplash-1-1.png" alt="sofa" />
        <img class="sm:hidden w-full" src="https://i.ibb.co/B6qwqPT/jason-wang-Nx-Awry-Abt-Iw-unsplash-1.png" alt="sofa" />
        <div class="absolute sm:bottom-8 bottom-4 pr-10 sm:pr-0 left-4 sm:left-8 flex justify-start items-start">
          <p class="text-3xl sm:text-4xl font-semibold leading-9 text-white">Range Comfort Sofas</p>
        </div>
      </div>
    </div>
    <div class="mt-10 grid lg:grid-cols-2 gap-x-8 gap-y-8 items-center">
      <div class="group group-hover:bg-opacity-60 transition duration-500 relative bg-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 sm:p-28 py-36 px-10 flex justify-center items-center">
        <img class="group-hover:opacity-60 transition duration-500" src="https://i.ibb.co/q79KfQr/pexels-pixabay-276583-removebg-preview-1.png" alt="sofa-2" />
        <div class="absolute sm:top-8 top-4 left-4 sm:left-8 flex justify-start items-start flex-col space-y-2">
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl leading-5 text-gray-600 dark:text-white">Sectional Sofa</p>
          </div>
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl font-semibold leading-5 text-gray-800 dark:text-white"></p>
          </div>
        </div>
        <div class="group-hover:opacity-60 transition duration-500 absolute bottom-8 right-8 flex justify-start items-start flex-row space-x-2">
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
        </div>
        <div class="flex flex-col bottom-8 left-8 space-y-4 absolute opacity-0 group-hover:opacity-100 transition duration-500">
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM15 13H13V15C13 15.2652 12.8946 15.5196 12.7071 15.7071C12.5196 15.8946 12.2652 16 12 16C11.7348 16 11.4804 15.8946 11.2929 15.7071C11.1054 15.5196 11 15.2652 11 15V13H9C8.73479 13 8.48043 12.8946 8.2929 12.7071C8.10536 12.5196 8 12.2652 8 12C8 11.7348 8.10536 11.4804 8.2929 11.2929C8.48043 11.1054 8.73479 11 9 11H11V9C11 8.73478 11.1054 8.48043 11.2929 8.29289C11.4804 8.10536 11.7348 8 12 8C12.2652 8 12.5196 8.10536 12.7071 8.29289C12.8946 8.48043 13 8.73478 13 9V11H15C15.2652 11 15.5196 11.1054 15.7071 11.2929C15.8946 11.4804 16 11.7348 16 12C16 12.2652 15.8946 12.5196 15.7071 12.7071C15.5196 12.8946 15.2652 13 15 13Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5Z" fill="currentColor" />
              <path d="M21.8701 11.5C21.2301 10.39 17.7101 4.82001 11.7301 5.00001C6.20007 5.14001 3.00007 10 2.13007 11.5C2.0423 11.652 1.99609 11.8245 1.99609 12C1.99609 12.1755 2.0423 12.348 2.13007 12.5C2.76007 13.59 6.13007 19 12.0201 19H12.2701C17.8001 18.86 21.0101 14 21.8701 12.5C21.9578 12.348 22.004 12.1755 22.004 12C22.004 11.8245 21.9578 11.652 21.8701 11.5ZM12.0001 15.5C11.3078 15.5 10.6311 15.2947 10.0556 14.9102C9.48 14.5256 9.0314 13.9789 8.76649 13.3394C8.50158 12.6999 8.43227 11.9961 8.56732 11.3172C8.70237 10.6383 9.03571 10.0146 9.52519 9.52514C10.0147 9.03565 10.6383 8.70231 11.3173 8.56726C11.9962 8.43221 12.6999 8.50152 13.3395 8.76643C13.979 9.03134 14.5256 9.47994 14.9102 10.0555C15.2948 10.6311 15.5001 11.3078 15.5001 12C15.5001 12.9283 15.1313 13.8185 14.4749 14.4749C13.8186 15.1313 12.9283 15.5 12.0001 15.5Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 21C11.8684 21.0008 11.7379 20.9755 11.6161 20.9258C11.4943 20.876 11.3834 20.8027 11.29 20.71L3.51999 12.93C2.54536 11.9452 1.99866 10.6156 1.99866 9.23C1.99866 7.84443 2.54536 6.51482 3.51999 5.53C4.50226 4.55051 5.83283 4.00047 7.21999 4.00047C8.60716 4.00047 9.93773 4.55051 10.92 5.53L12 6.61L13.08 5.53C14.0623 4.55051 15.3928 4.00047 16.78 4.00047C18.1672 4.00047 19.4977 4.55051 20.48 5.53C21.4546 6.51482 22.0013 7.84443 22.0013 9.23C22.0013 10.6156 21.4546 11.9452 20.48 12.93L12.71 20.71C12.6166 20.8027 12.5057 20.876 12.3839 20.9258C12.2621 20.9755 12.1316 21.0008 12 21Z" fill="currentColor" />
            </svg>
          </button>
        </div>
      </div>

      <div class="group group-hover:bg-opacity-60 transition duration-500 relative bg-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 sm:p-28 py-36 px-10 flex justify-center items-center">
        <img class="group-hover:opacity-60 transition duration-500" src="https://i.ibb.co/3BbZvtQ/pexels-andrea-piacquadio-3757055-removebg-preview-1.png" alt="sofa-3" />
        <div class="absolute sm:top-8 top-4 left-4 sm:left-8 flex justify-start items-start flex-col space-y-2">
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl leading-5 text-gray-600 dark:text-white">Two Seater Sofa</p>
          </div>
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl font-semibold leading-5 text-gray-800 dark:text-white"></p>
          </div>
        </div>
        <div class="group-hover:opacity-60 transition duration-500 absolute bottom-8 right-8 flex justify-start items-start flex-row space-x-2">
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
        </div>
        <div class="flex flex-col bottom-8 left-8 space-y-4 absolute opacity-0 group-hover:opacity-100 transition duration-500">
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM15 13H13V15C13 15.2652 12.8946 15.5196 12.7071 15.7071C12.5196 15.8946 12.2652 16 12 16C11.7348 16 11.4804 15.8946 11.2929 15.7071C11.1054 15.5196 11 15.2652 11 15V13H9C8.73479 13 8.48043 12.8946 8.2929 12.7071C8.10536 12.5196 8 12.2652 8 12C8 11.7348 8.10536 11.4804 8.2929 11.2929C8.48043 11.1054 8.73479 11 9 11H11V9C11 8.73478 11.1054 8.48043 11.2929 8.29289C11.4804 8.10536 11.7348 8 12 8C12.2652 8 12.5196 8.10536 12.7071 8.29289C12.8946 8.48043 13 8.73478 13 9V11H15C15.2652 11 15.5196 11.1054 15.7071 11.2929C15.8946 11.4804 16 11.7348 16 12C16 12.2652 15.8946 12.5196 15.7071 12.7071C15.5196 12.8946 15.2652 13 15 13Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5Z" fill="currentColor" />
              <path d="M21.8701 11.5C21.2301 10.39 17.7101 4.82001 11.7301 5.00001C6.20007 5.14001 3.00007 10 2.13007 11.5C2.0423 11.652 1.99609 11.8245 1.99609 12C1.99609 12.1755 2.0423 12.348 2.13007 12.5C2.76007 13.59 6.13007 19 12.0201 19H12.2701C17.8001 18.86 21.0101 14 21.8701 12.5C21.9578 12.348 22.004 12.1755 22.004 12C22.004 11.8245 21.9578 11.652 21.8701 11.5ZM12.0001 15.5C11.3078 15.5 10.6311 15.2947 10.0556 14.9102C9.48 14.5256 9.0314 13.9789 8.76649 13.3394C8.50158 12.6999 8.43227 11.9961 8.56732 11.3172C8.70237 10.6383 9.03571 10.0146 9.52519 9.52514C10.0147 9.03565 10.6383 8.70231 11.3173 8.56726C11.9962 8.43221 12.6999 8.50152 13.3395 8.76643C13.979 9.03134 14.5256 9.47994 14.9102 10.0555C15.2948 10.6311 15.5001 11.3078 15.5001 12C15.5001 12.9283 15.1313 13.8185 14.4749 14.4749C13.8186 15.1313 12.9283 15.5 12.0001 15.5Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 21C11.8684 21.0008 11.7379 20.9755 11.6161 20.9258C11.4943 20.876 11.3834 20.8027 11.29 20.71L3.51999 12.93C2.54536 11.9452 1.99866 10.6156 1.99866 9.23C1.99866 7.84443 2.54536 6.51482 3.51999 5.53C4.50226 4.55051 5.83283 4.00047 7.21999 4.00047C8.60716 4.00047 9.93773 4.55051 10.92 5.53L12 6.61L13.08 5.53C14.0623 4.55051 15.3928 4.00047 16.78 4.00047C18.1672 4.00047 19.4977 4.55051 20.48 5.53C21.4546 6.51482 22.0013 7.84443 22.0013 9.23C22.0013 10.6156 21.4546 11.9452 20.48 12.93L12.71 20.71C12.6166 20.8027 12.5057 20.876 12.3839 20.9258C12.2621 20.9755 12.1316 21.0008 12 21Z" fill="currentColor" />
            </svg>
          </button>
        </div>
      </div>

      <div class="group group-hover:bg-opacity-60 transition duration-500 relative bg-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 sm:p-28 py-36 px-10 flex justify-center items-center">
        <img class="group-hover:opacity-60 transition duration-500" src="https://i.ibb.co/DgFfGcm/paul-weaver-n-Wid-MEQsn-AQ-unsplash-removebg-preview-1.png" alt="sofa-4" />
        <div class="absolute sm:top-8 top-4 left-4 sm:left-8 flex justify-start items-start flex-col space-y-2">
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl leading-5 text-gray-600 dark:text-white">Sectional Sofa</p>
          </div>
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl font-semibold leading-5 text-gray-800 dark:text-white"></p>
          </div>
        </div>
        <div class="group-hover:opacity-60 transition duration-500 absolute bottom-8 right-8 flex justify-start items-start flex-row space-x-2">
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
        </div>
        <div class="flex flex-col bottom-8 left-8 space-y-4 absolute opacity-0 group-hover:opacity-100 transition duration-500">
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM15 13H13V15C13 15.2652 12.8946 15.5196 12.7071 15.7071C12.5196 15.8946 12.2652 16 12 16C11.7348 16 11.4804 15.8946 11.2929 15.7071C11.1054 15.5196 11 15.2652 11 15V13H9C8.73479 13 8.48043 12.8946 8.2929 12.7071C8.10536 12.5196 8 12.2652 8 12C8 11.7348 8.10536 11.4804 8.2929 11.2929C8.48043 11.1054 8.73479 11 9 11H11V9C11 8.73478 11.1054 8.48043 11.2929 8.29289C11.4804 8.10536 11.7348 8 12 8C12.2652 8 12.5196 8.10536 12.7071 8.29289C12.8946 8.48043 13 8.73478 13 9V11H15C15.2652 11 15.5196 11.1054 15.7071 11.2929C15.8946 11.4804 16 11.7348 16 12C16 12.2652 15.8946 12.5196 15.7071 12.7071C15.5196 12.8946 15.2652 13 15 13Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5Z" fill="currentColor" />
              <path d="M21.8701 11.5C21.2301 10.39 17.7101 4.82001 11.7301 5.00001C6.20007 5.14001 3.00007 10 2.13007 11.5C2.0423 11.652 1.99609 11.8245 1.99609 12C1.99609 12.1755 2.0423 12.348 2.13007 12.5C2.76007 13.59 6.13007 19 12.0201 19H12.2701C17.8001 18.86 21.0101 14 21.8701 12.5C21.9578 12.348 22.004 12.1755 22.004 12C22.004 11.8245 21.9578 11.652 21.8701 11.5ZM12.0001 15.5C11.3078 15.5 10.6311 15.2947 10.0556 14.9102C9.48 14.5256 9.0314 13.9789 8.76649 13.3394C8.50158 12.6999 8.43227 11.9961 8.56732 11.3172C8.70237 10.6383 9.03571 10.0146 9.52519 9.52514C10.0147 9.03565 10.6383 8.70231 11.3173 8.56726C11.9962 8.43221 12.6999 8.50152 13.3395 8.76643C13.979 9.03134 14.5256 9.47994 14.9102 10.0555C15.2948 10.6311 15.5001 11.3078 15.5001 12C15.5001 12.9283 15.1313 13.8185 14.4749 14.4749C13.8186 15.1313 12.9283 15.5 12.0001 15.5Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 21C11.8684 21.0008 11.7379 20.9755 11.6161 20.9258C11.4943 20.876 11.3834 20.8027 11.29 20.71L3.51999 12.93C2.54536 11.9452 1.99866 10.6156 1.99866 9.23C1.99866 7.84443 2.54536 6.51482 3.51999 5.53C4.50226 4.55051 5.83283 4.00047 7.21999 4.00047C8.60716 4.00047 9.93773 4.55051 10.92 5.53L12 6.61L13.08 5.53C14.0623 4.55051 15.3928 4.00047 16.78 4.00047C18.1672 4.00047 19.4977 4.55051 20.48 5.53C21.4546 6.51482 22.0013 7.84443 22.0013 9.23C22.0013 10.6156 21.4546 11.9452 20.48 12.93L12.71 20.71C12.6166 20.8027 12.5057 20.876 12.3839 20.9258C12.2621 20.9755 12.1316 21.0008 12 21Z" fill="currentColor" />
            </svg>
          </button>
        </div>
      </div>

      <div class="group group-hover:bg-opacity-60 transition duration-500 relative bg-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 sm:p-28 py-36 px-10 flex justify-center items-center">
        <img class="group-hover:opacity-60 transition duration-500" src="https://i.ibb.co/K6PL38P/pexels-pixabay-276566-removebg-preview-1.png" alt="sofa-5" />
        <div class="absolute sm:top-8 top-4 left-4 sm:left-8 flex justify-start items-start flex-col space-y-2">
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl leading-5 text-gray-600 dark:text-white">Sectional Sofa</p>
          </div>
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl font-semibold leading-5 text-gray-800 dark:text-white"></p>
          </div>
        </div>
        <div class="group-hover:opacity-60 transition duration-500 absolute bottom-8 right-8 flex justify-start items-start flex-row space-x-2">
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
        </div>
        <div class="flex flex-col bottom-8 left-8 space-y-4 absolute opacity-0 group-hover:opacity-100 transition duration-500">
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM15 13H13V15C13 15.2652 12.8946 15.5196 12.7071 15.7071C12.5196 15.8946 12.2652 16 12 16C11.7348 16 11.4804 15.8946 11.2929 15.7071C11.1054 15.5196 11 15.2652 11 15V13H9C8.73479 13 8.48043 12.8946 8.2929 12.7071C8.10536 12.5196 8 12.2652 8 12C8 11.7348 8.10536 11.4804 8.2929 11.2929C8.48043 11.1054 8.73479 11 9 11H11V9C11 8.73478 11.1054 8.48043 11.2929 8.29289C11.4804 8.10536 11.7348 8 12 8C12.2652 8 12.5196 8.10536 12.7071 8.29289C12.8946 8.48043 13 8.73478 13 9V11H15C15.2652 11 15.5196 11.1054 15.7071 11.2929C15.8946 11.4804 16 11.7348 16 12C16 12.2652 15.8946 12.5196 15.7071 12.7071C15.5196 12.8946 15.2652 13 15 13Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5Z" fill="currentColor" />
              <path d="M21.8701 11.5C21.2301 10.39 17.7101 4.82001 11.7301 5.00001C6.20007 5.14001 3.00007 10 2.13007 11.5C2.0423 11.652 1.99609 11.8245 1.99609 12C1.99609 12.1755 2.0423 12.348 2.13007 12.5C2.76007 13.59 6.13007 19 12.0201 19H12.2701C17.8001 18.86 21.0101 14 21.8701 12.5C21.9578 12.348 22.004 12.1755 22.004 12C22.004 11.8245 21.9578 11.652 21.8701 11.5ZM12.0001 15.5C11.3078 15.5 10.6311 15.2947 10.0556 14.9102C9.48 14.5256 9.0314 13.9789 8.76649 13.3394C8.50158 12.6999 8.43227 11.9961 8.56732 11.3172C8.70237 10.6383 9.03571 10.0146 9.52519 9.52514C10.0147 9.03565 10.6383 8.70231 11.3173 8.56726C11.9962 8.43221 12.6999 8.50152 13.3395 8.76643C13.979 9.03134 14.5256 9.47994 14.9102 10.0555C15.2948 10.6311 15.5001 11.3078 15.5001 12C15.5001 12.9283 15.1313 13.8185 14.4749 14.4749C13.8186 15.1313 12.9283 15.5 12.0001 15.5Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 21C11.8684 21.0008 11.7379 20.9755 11.6161 20.9258C11.4943 20.876 11.3834 20.8027 11.29 20.71L3.51999 12.93C2.54536 11.9452 1.99866 10.6156 1.99866 9.23C1.99866 7.84443 2.54536 6.51482 3.51999 5.53C4.50226 4.55051 5.83283 4.00047 7.21999 4.00047C8.60716 4.00047 9.93773 4.55051 10.92 5.53L12 6.61L13.08 5.53C14.0623 4.55051 15.3928 4.00047 16.78 4.00047C18.1672 4.00047 19.4977 4.55051 20.48 5.53C21.4546 6.51482 22.0013 7.84443 22.0013 9.23C22.0013 10.6156 21.4546 11.9452 20.48 12.93L12.71 20.71C12.6166 20.8027 12.5057 20.876 12.3839 20.9258C12.2621 20.9755 12.1316 21.0008 12 21Z" fill="currentColor" />
            </svg>
          </button>
        </div>
        <div class="absolute top-4 right-6">
          <p class="text-base leading-4 pb-0.5 text-gray-600 dark:text-white border-b-2 border-gray-600">New</p>
        </div>
      </div>

      <div class="group group-hover:bg-opacity-60 transition duration-500 relative bg-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 sm:p-28 py-36 px-10 flex justify-center items-center">
        <img class="group-hover:opacity-60 transition duration-500" src="https://i.ibb.co/zP9sWqP/phillip-goldsberry-f-Zule-Efe-A1-Q-unsplash-1-removebg-preview-1.png" alt="sofa-6" />
        <div class="absolute sm:top-8 top-4 left-4 sm:left-8 flex justify-start items-start flex-col space-y-2">
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl leading-5 text-gray-600 dark:text-white">Sectional Sofa</p>
          </div>
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl font-semibold leading-5 text-gray-800 dark:text-white"></p>
          </div>
        </div>
        <div class="group-hover:opacity-60 transition duration-500 absolute bottom-8 right-8 flex justify-start items-start flex-row space-x-2">
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
        </div>
        <div class="flex flex-col bottom-8 left-8 space-y-4 absolute opacity-0 group-hover:opacity-100 transition duration-500">
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM15 13H13V15C13 15.2652 12.8946 15.5196 12.7071 15.7071C12.5196 15.8946 12.2652 16 12 16C11.7348 16 11.4804 15.8946 11.2929 15.7071C11.1054 15.5196 11 15.2652 11 15V13H9C8.73479 13 8.48043 12.8946 8.2929 12.7071C8.10536 12.5196 8 12.2652 8 12C8 11.7348 8.10536 11.4804 8.2929 11.2929C8.48043 11.1054 8.73479 11 9 11H11V9C11 8.73478 11.1054 8.48043 11.2929 8.29289C11.4804 8.10536 11.7348 8 12 8C12.2652 8 12.5196 8.10536 12.7071 8.29289C12.8946 8.48043 13 8.73478 13 9V11H15C15.2652 11 15.5196 11.1054 15.7071 11.2929C15.8946 11.4804 16 11.7348 16 12C16 12.2652 15.8946 12.5196 15.7071 12.7071C15.5196 12.8946 15.2652 13 15 13Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5Z" fill="currentColor" />
              <path d="M21.8701 11.5C21.2301 10.39 17.7101 4.82001 11.7301 5.00001C6.20007 5.14001 3.00007 10 2.13007 11.5C2.0423 11.652 1.99609 11.8245 1.99609 12C1.99609 12.1755 2.0423 12.348 2.13007 12.5C2.76007 13.59 6.13007 19 12.0201 19H12.2701C17.8001 18.86 21.0101 14 21.8701 12.5C21.9578 12.348 22.004 12.1755 22.004 12C22.004 11.8245 21.9578 11.652 21.8701 11.5ZM12.0001 15.5C11.3078 15.5 10.6311 15.2947 10.0556 14.9102C9.48 14.5256 9.0314 13.9789 8.76649 13.3394C8.50158 12.6999 8.43227 11.9961 8.56732 11.3172C8.70237 10.6383 9.03571 10.0146 9.52519 9.52514C10.0147 9.03565 10.6383 8.70231 11.3173 8.56726C11.9962 8.43221 12.6999 8.50152 13.3395 8.76643C13.979 9.03134 14.5256 9.47994 14.9102 10.0555C15.2948 10.6311 15.5001 11.3078 15.5001 12C15.5001 12.9283 15.1313 13.8185 14.4749 14.4749C13.8186 15.1313 12.9283 15.5 12.0001 15.5Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 21C11.8684 21.0008 11.7379 20.9755 11.6161 20.9258C11.4943 20.876 11.3834 20.8027 11.29 20.71L3.51999 12.93C2.54536 11.9452 1.99866 10.6156 1.99866 9.23C1.99866 7.84443 2.54536 6.51482 3.51999 5.53C4.50226 4.55051 5.83283 4.00047 7.21999 4.00047C8.60716 4.00047 9.93773 4.55051 10.92 5.53L12 6.61L13.08 5.53C14.0623 4.55051 15.3928 4.00047 16.78 4.00047C18.1672 4.00047 19.4977 4.55051 20.48 5.53C21.4546 6.51482 22.0013 7.84443 22.0013 9.23C22.0013 10.6156 21.4546 11.9452 20.48 12.93L12.71 20.71C12.6166 20.8027 12.5057 20.876 12.3839 20.9258C12.2621 20.9755 12.1316 21.0008 12 21Z" fill="currentColor" />
            </svg>
          </button>
        </div>
      </div>

      <div class="group group-hover:bg-opacity-60 transition duration-500 relative bg-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 sm:p-28 py-36 px-10 flex justify-center items-center">
        <img class="group-hover:opacity-60 transition duration-500" src="https://i.ibb.co/SPyYgjw/pexels-martin-p-chy-1866149-removebg-preview-1.png" alt="sofa-7" />
        <div class="absolute sm:top-8 top-4 left-4 sm:left-8 flex justify-start items-start flex-col space-y-2">
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl leading-5 text-gray-600 dark:text-white">Sectional Sofa</p>
          </div>
          <div>
            <p class="group-hover:opacity-60 transition duration-500 text-xl font-semibold leading-5 text-gray-800 dark:text-white"></p>
          </div>
        </div>
        <div class="group-hover:opacity-60 transition duration-500 absolute bottom-8 right-8 flex justify-start items-start flex-row space-x-2">
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
          <button class="bg-white border rounded-full focus:bg-gray-800 border-gray-600 p-1.5"></button>
        </div>
        <div class="flex flex-col bottom-8 left-8 space-y-4 absolute opacity-0 group-hover:opacity-100 transition duration-500">
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM15 13H13V15C13 15.2652 12.8946 15.5196 12.7071 15.7071C12.5196 15.8946 12.2652 16 12 16C11.7348 16 11.4804 15.8946 11.2929 15.7071C11.1054 15.5196 11 15.2652 11 15V13H9C8.73479 13 8.48043 12.8946 8.2929 12.7071C8.10536 12.5196 8 12.2652 8 12C8 11.7348 8.10536 11.4804 8.2929 11.2929C8.48043 11.1054 8.73479 11 9 11H11V9C11 8.73478 11.1054 8.48043 11.2929 8.29289C11.4804 8.10536 11.7348 8 12 8C12.2652 8 12.5196 8.10536 12.7071 8.29289C12.8946 8.48043 13 8.73478 13 9V11H15C15.2652 11 15.5196 11.1054 15.7071 11.2929C15.8946 11.4804 16 11.7348 16 12C16 12.2652 15.8946 12.5196 15.7071 12.7071C15.5196 12.8946 15.2652 13 15 13Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5Z" fill="currentColor" />
              <path d="M21.8701 11.5C21.2301 10.39 17.7101 4.82001 11.7301 5.00001C6.20007 5.14001 3.00007 10 2.13007 11.5C2.0423 11.652 1.99609 11.8245 1.99609 12C1.99609 12.1755 2.0423 12.348 2.13007 12.5C2.76007 13.59 6.13007 19 12.0201 19H12.2701C17.8001 18.86 21.0101 14 21.8701 12.5C21.9578 12.348 22.004 12.1755 22.004 12C22.004 11.8245 21.9578 11.652 21.8701 11.5ZM12.0001 15.5C11.3078 15.5 10.6311 15.2947 10.0556 14.9102C9.48 14.5256 9.0314 13.9789 8.76649 13.3394C8.50158 12.6999 8.43227 11.9961 8.56732 11.3172C8.70237 10.6383 9.03571 10.0146 9.52519 9.52514C10.0147 9.03565 10.6383 8.70231 11.3173 8.56726C11.9962 8.43221 12.6999 8.50152 13.3395 8.76643C13.979 9.03134 14.5256 9.47994 14.9102 10.0555C15.2948 10.6311 15.5001 11.3078 15.5001 12C15.5001 12.9283 15.1313 13.8185 14.4749 14.4749C13.8186 15.1313 12.9283 15.5 12.0001 15.5Z" fill="currentColor" />
            </svg>
          </button>
          <button>
            <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 21C11.8684 21.0008 11.7379 20.9755 11.6161 20.9258C11.4943 20.876 11.3834 20.8027 11.29 20.71L3.51999 12.93C2.54536 11.9452 1.99866 10.6156 1.99866 9.23C1.99866 7.84443 2.54536 6.51482 3.51999 5.53C4.50226 4.55051 5.83283 4.00047 7.21999 4.00047C8.60716 4.00047 9.93773 4.55051 10.92 5.53L12 6.61L13.08 5.53C14.0623 4.55051 15.3928 4.00047 16.78 4.00047C18.1672 4.00047 19.4977 4.55051 20.48 5.53C21.4546 6.51482 22.0013 7.84443 22.0013 9.23C22.0013 10.6156 21.4546 11.9452 20.48 12.93L12.71 20.71C12.6166 20.8027 12.5057 20.876 12.3839 20.9258C12.2621 20.9755 12.1316 21.0008 12 21Z" fill="currentColor" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    <div class="flex justify-end items-end mt-12">
      <div class="flex flex-row items-center justify-center space-x-8">
        <button class="text-base leading-none text-gray-800 dark:text-white border-b-2 border-transparent focus:outline-none focus:border-gray-800">
          <p>1</p>
        </button>
        <button class="text-base leading-none text-gray-800 dark:text-white border-b-2 border-transparent focus:outline-none focus:border-gray-800">
          <p>2</p>
        </button>
        <button class="text-base leading-none text-gray-800 dark:text-white border-b-2 border-transparent focus:outline-none focus:border-gray-800">
          <p>3</p>
        </button>
        <button class="flex justify-center items-center">
          <svg class="dark:text-white" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </button>
      </div>
    </div>
  </div>

</div>''', '''<!-- tailwind.config.js -->
module.exports = {
    theme: {
        extend: {
            fontFamily: {
                'source-sans-pro': ['Source Sans Pro'],
                'mitr': ['Mitr'],
                'roboto-slab': ['Roboto Slab'],
            },
        },
    },
};



<!-- component -->
<link href="https://fonts.googleapis.com/css?family=Mitr|Roboto+Slab|Source+Sans+Pro&display=swap" rel="stylesheet">
<script src="https://premium-tailwindcomponents.netlify.app/assets/build/js/main.js?id=8c11b7cf78ebea1b5aed"></script>

<div class="bg-indigo-900 relative overflow-hidden">
    <div class="inset-0 bg-black opacity-25 absolute"></div>
    <header class="absolute top-0 left-0 right-0 z-20">
        <nav class="container mx-auto px-6 md:px-12 py-4" x-data="{ open: false }">
            <div class="md:flex justify-between items-center">
                <div class="flex justify-between items-center">
                    <a href="#" class="text-white">
                        <svg class="w-6 mr-2 fill-current" xmlns="http://www.w3.org/2000/svg" data-name="Capa 1" viewBox="0 0 16.16 12.57"><defs/><path d="M14.02 4.77v7.8H9.33V8.8h-2.5v3.77H2.14v-7.8h11.88z"/><path d="M16.16 5.82H0L8.08 0l8.08 5.82z"/></svg>
                    </a>

                    <div class="md:hidden">
                        <button @click="open = !open" class="text-white focus:outline-none">
                            <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path x-show="open === false" d="M4 6H20M4 12H20M4 18H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path x-show="open === true" d="M6 18L18 6M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </button>
                    </div>
                </div>

                <div class="hidden md:flex items-center">
                    <a class="text-sm uppercase mx-3 text-white cursor-pointer hover:text-indigo-600">About us</a>
                    <a class="text-sm uppercase mx-3 text-white cursor-pointer hover:text-indigo-600">Calendar</a>
                    <a class="text-sm uppercase mx-3 text-white cursor-pointer hover:text-indigo-600">Contact us</a>
                </div>
            </div>

            <div x-show="open === true" class="md:hidden flex flex-col w-full z-40 bg-indigo-600 rounded mt-4 py-2 overflow-hidden">
                <a class="font-mitr text-sm uppercase text-gray-200 py-2 px-2 hover:bg-indigo-500">About us</a>
                <a class="font-mitr text-sm uppercase text-gray-200 py-2 px-2 hover:bg-indigo-500">Calendar</a>
                <a class="font-mitr text-sm uppercase text-gray-200 py-2 px-2 hover:bg-indigo-500">Contact us</a>
            </div>
        </nav>
    </header>

    <div class="container mx-auto px-6 md:px-12 relative z-10 flex items-center py-24 xl:py-40">
        <div class="lg:w-3/5 xl:w-2/5 flex flex-col items-start relative z-10">
            <span class="font-mitr uppercase text-indigo-500">Lorem ipsum</span>

            <h1 class="font-roboto-slab text-4xl sm:text-6xl text-red-400 leading-tight mt-4">Let's go <br> back to school</h1>

            <div class="max-w-md">
                <p class="font-source-sans-pro text-indigo-500 mt-6 text-lg">Lorem ipsum dolor sit amet consectetur adipiscing elit tincidunt cras sociis, parturient enim montes.</p>
            </div>

            <a href="#" class="block bg-indigo-500 hover:bg-indigo-400 py-2 px-4 rounded-full text-sm font-mitr text-white uppercase mt-10">Get started</a>
        </div>

        <svg class="hidden sm:block absolute bottom-0 right-0 -mr-40 lg:mr-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 645.06 372.73"><defs/><defs><radialGradient id="a" cx="416.96" cy="273.37" r="226.21" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6e3f63"/><stop offset=".15" stop-color="#633d62"/><stop offset=".41" stop-color="#473660"/><stop offset=".5" stop-color="#3b335f"/><stop offset=".6" stop-color="#38315c" stop-opacity=".88"/><stop offset=".76" stop-color="#302b55" stop-opacity=".57"/><stop offset=".97" stop-color="#242249" stop-opacity=".07"/><stop offset="1" stop-color="#222147" stop-opacity="0"/></radialGradient></defs><g data-name="Capa 1"><path fill="url(#a)" d="M645.06 0v372.73H4.2L0 0h645.06z"/><path fill="#d29b72" d="M487.31 222.05a2.41 2.41 0 014.81 0c0 1.33-1.08 49.27-2.41 49.27s-2.4-47.94-2.4-49.27z"/><circle cx="489.71" cy="222.05" r="1.69" fill="#e8c275"/><path fill="#f3eece" d="M488.63 222.05a1.08 1.08 0 012.16 0 1.08 1.08 0 11-2.16 0z"/><path fill="#d29b72" d="M338.77 252.5a1.39 1.39 0 012.77 0c0 .76-.62 28.28-1.38 28.28s-1.39-27.52-1.39-28.28z"/><path fill="#e8c275" d="M339.19 252.5a1 1 0 111 1 1 1 0 01-1-1z"/><circle cx="340.16" cy="252.5" r=".62" fill="#f3eece"/><g opacity=".5"><path fill="#d29b72" d="M370.16 172.82a1.8 1.8 0 013.6 0c0 1-.8 36.87-1.8 36.87s-1.8-35.88-1.8-36.87z"/><path fill="#e8c275" d="M370.7 172.82a1.26 1.26 0 111.26 1.26 1.26 1.26 0 01-1.26-1.26z"/><circle cx="371.96" cy="172.82" r=".81" fill="#f3eece"/></g><path fill="#f3eece" d="M466.22 225.08a1.29 1.29 0 11-1.28-1.28 1.28 1.28 0 011.28 1.28zM350.22 186a1.29 1.29 0 01-2.57 0 1.29 1.29 0 112.57 0z"/><circle cx="497.5" cy="176.37" r="1.29" fill="#f3eece"/><path fill="#f3eece" d="M370.17 248.47a1.29 1.29 0 11-1.29-1.29 1.28 1.28 0 011.29 1.29z"/><circle cx="277.03" cy="215.66" r="1.29" fill="#f3eece"/><path fill="#fff" d="M330.41 224.8a.65.65 0 11-.64-.64.65.65 0 01.64.64zM469.82 227.34a.65.65 0 11-.65-.64.65.65 0 01.65.64z"/><circle cx="260.82" cy="273.25" r="1.29" fill="#f3eece"/><path fill="#fff" d="M265.7 275.52a.65.65 0 11-.64-.65.64.64 0 01.64.65zM532.33 266.64a.65.65 0 11-.65-.65.65.65 0 01.65.65z"/><circle cx="528.92" cy="271.89" r="1.29" fill="#f3eece"/><path fill="#fff" d="M557.69 179.87a.64.64 0 11-.47 1.2.64.64 0 01.47-1.2z"/><path fill="#f3eece" d="M561.81 183.76a1.29 1.29 0 11-1.67.73 1.29 1.29 0 011.67-.73zM540 143.22a1.29 1.29 0 11-1.67.73 1.29 1.29 0 011.67-.73z"/><path fill="#fff" d="M281.65 146.15a.64.64 0 01-.47 1.2.64.64 0 11.47-1.2z"/><path fill="#f3eece" d="M285.76 150a1.29 1.29 0 11-1.66.73 1.29 1.29 0 011.66-.73z"/><circle cx="333.34" cy="222.07" r="1.29" fill="#f3eece"/><circle cx="338.06" cy="135.84" r="13.93" fill="none" stroke="#5c4f84" stroke-miterlimit="10" stroke-width=".735" transform="rotate(-22.72 338.064 135.833)"/><circle cx="304.19" cy="187.52" r="10.74" fill="none" stroke="#5c4f84" stroke-miterlimit="10" stroke-width=".735" transform="rotate(-80.82 304.168 187.524)"/><circle cx="509.71" cy="183.41" r="3.98" fill="#fff" fill-opacity=".2"/><path fill="#fff" fill-opacity=".3" d="M509.71 188.07a.68.68 0 01-.68-.67v-8a.68.68 0 01.68-.67.67.67 0 01.67.67v8a.67.67 0 01-.67.67z"/><path fill="#fff" fill-opacity=".3" d="M514.37 183.41a.67.67 0 01-.67.67h-8a.67.67 0 01-.67-.67.68.68 0 01.67-.68h8a.68.68 0 01.67.68z"/><path fill="#fff" d="M512.53 183.41a.67.67 0 01-.67.67h-4.3a.67.67 0 01-.67-.67.68.68 0 01.67-.68h4.3a.68.68 0 01.67.68z"/><path fill="#fff" d="M509.71 186.23a.68.68 0 01-.68-.67v-4.3a.68.68 0 01.68-.67.67.67 0 01.67.67v4.3a.67.67 0 01-.67.67z"/><path fill="#fff" fill-opacity=".2" d="M505.06 114.25a4 4 0 114 4 4 4 0 01-4-4z"/><path fill="#fff" fill-opacity=".3" d="M509 118.91a.67.67 0 01-.67-.67v-8a.68.68 0 01.67-.68.68.68 0 01.68.68v8a.67.67 0 01-.68.67z"/><path fill="#fff" fill-opacity=".3" d="M513.7 114.25a.67.67 0 01-.68.67h-8a.67.67 0 01-.68-.67.67.67 0 01.68-.68h8a.67.67 0 01.68.68z"/><path fill="#fff" d="M511.86 114.25a.67.67 0 01-.68.67h-4.29a.67.67 0 01-.68-.67.67.67 0 01.68-.68h4.29a.67.67 0 01.68.68z"/><path fill="#fff" d="M509 117.07a.67.67 0 01-.67-.67v-4.3a.68.68 0 01.67-.68.68.68 0 01.68.68v4.3a.67.67 0 01-.68.67z"/><path fill="#fff" fill-opacity=".2" d="M288 251.91a4 4 0 114 4 4 4 0 01-4-4z"/><path fill="#fff" fill-opacity=".3" d="M292 256.57a.67.67 0 01-.67-.67v-8a.68.68 0 01.67-.68.68.68 0 01.67.68v8a.67.67 0 01-.67.67z"/><path fill="#fff" fill-opacity=".3" d="M296.61 251.91a.67.67 0 01-.67.67h-8a.67.67 0 01-.67-.67.67.67 0 01.67-.68h8a.67.67 0 01.67.68z"/><path fill="#fff" d="M294.77 251.91a.67.67 0 01-.67.67h-4.3a.67.67 0 01-.67-.67.67.67 0 01.67-.68h4.3a.67.67 0 01.67.68z"/><path fill="#fff" d="M292 254.73a.67.67 0 01-.67-.67v-4.3a.68.68 0 01.67-.68.68.68 0 01.67.68v4.3a.67.67 0 01-.67.67z"/><path fill="#fff" fill-opacity=".2" d="M336.2 181.15a4 4 0 114 4 4 4 0 01-4-4z"/><path fill="#fff" fill-opacity=".3" d="M340.17 185.81a.67.67 0 01-.67-.67v-8a.67.67 0 01.67-.67.67.67 0 01.68.67v8a.67.67 0 01-.68.67z"/><path fill="#fff" fill-opacity=".3" d="M344.84 181.15a.68.68 0 01-.68.67h-8a.67.67 0 01-.67-.67.67.67 0 01.67-.67h8a.68.68 0 01.68.67z"/><path fill="#fff" d="M343 181.15a.68.68 0 01-.68.67H338a.67.67 0 01-.67-.67.67.67 0 01.67-.67h4.3a.68.68 0 01.7.67z"/><path fill="#fff" d="M340.17 184a.67.67 0 01-.67-.67V179a.67.67 0 01.67-.67.67.67 0 01.68.67v4.3a.67.67 0 01-.68.7z"/><circle cx="337.46" cy="135.87" r="9.46" fill="#b96a51" transform="rotate(-81.16 337.446 135.873)"/><path fill="#a65054" d="M342.44 127.83a9.41 9.41 0 00-6.51-1.28 10.56 10.56 0 014.92 8.15c.63 5.79-4.19 10.36-4.41 10.56a9.45 9.45 0 006-17.43z"/><path fill="#854354" d="M341.94 128.33a8.78 8.78 0 01-4.06 16.24 9.32 9.32 0 002-16.78 9.55 9.55 0 00-1.35-.69 8.9 8.9 0 013.41 1.23z"/><path fill="#dbb07b" d="M331.05 141a3 3 0 114.09-1 3 3 0 01-4.09 1z" opacity=".3"/><path fill="#dbb07b" d="M330.81 139.82a1.71 1.71 0 112.35-.55 1.7 1.7 0 01-2.35.55zM333.64 133.24a3 3 0 114.09-1 3 3 0 01-4.09 1z" opacity=".3"/><path fill="#dbb07b" d="M333.42 131.79a1.6 1.6 0 112.2-.52 1.6 1.6 0 01-2.2.52zM329.81 134.58a1.47 1.47 0 112-.47 1.46 1.46 0 01-2 .47z" opacity=".3"/><path fill="#dbb07b" d="M329.78 134.1a.79.79 0 01-.25-1.09.79.79 0 011.34.83.79.79 0 01-1.09.26z" opacity=".3"/><path fill="#cd936d" d="M334.25 128.23a8 8 0 00-4.79 7.45 8.75 8.75 0 006.2 8.19 10.83 10.83 0 01-4.3-7.36 11.49 11.49 0 012.89-8.28z" opacity=".5"/><path fill="#dbb07b" d="M334.25 128.23s-4.82 2.58-4.43 7.76a9.78 9.78 0 005.84 7.88s-6.06-1.56-6.45-7.84a7.91 7.91 0 015.04-7.8z"/><path fill="#d8e5f4" d="M355.59 130.92c.41 1.13-3.17 3.51-8.73 6-2.3 1-4.94 2.1-7.77 3.11s-5.74 1.92-8.24 2.57c-5.77 1.51-9.93 1.9-10.32.78s2.73-3.21 7.69-5.54c.07.32.15.63.25.94-1.9 1.06-3 1.94-2.81 2.42s1.71.49 4 0a63.87 63.87 0 008.91-2.56 66.75 66.75 0 008.28-3.52c2.24-1.18 3.54-2.18 3.35-2.71s-1.68-.49-4 0c-.12-.3-.25-.59-.4-.88 5.53-1.36 9.41-1.68 9.79-.61z"/><path fill="#d59145" d="M355.65 131.29c.41 1.13-3.17 3.51-8.73 6-2.3 1-4.93 2.1-7.77 3.11s-5.74 1.91-8.24 2.57c-5.77 1.5-9.92 1.9-10.32.78s2.76-3.22 7.71-5.55a7.45 7.45 0 00.29.92c-1.91 1-3 2-2.87 2.45s1.71.49 4 0a66.76 66.76 0 008.91-2.56 65.14 65.14 0 008.28-3.53c2.24-1.17 3.54-2.17 3.35-2.7s-1.62-.51-3.91-.07a7.46 7.46 0 00-.35-.89c5.49-1.31 9.27-1.61 9.65-.53z"/><path fill="#edcf8e" d="M355.59 130.92c.41 1.13-3.17 3.51-8.73 6-2.3 1-4.94 2.1-7.77 3.11s-5.74 1.92-8.24 2.57c-5.77 1.51-9.93 1.9-10.32.78s2.73-3.21 7.69-5.54c.07.32.15.63.25.94-1.9 1.06-3 1.94-2.81 2.42s1.71.49 4 0a63.87 63.87 0 008.91-2.56 66.75 66.75 0 008.28-3.52c2.24-1.18 3.54-2.18 3.35-2.71s-1.68-.49-4 0c-.12-.3-.25-.59-.4-.88 5.53-1.36 9.41-1.68 9.79-.61z"/><path fill="#f5e5c2" d="M352.11 130.58c1.34 0 3.21-.35 3.13.67s-5.24 4.49-17.24 8.88c0 0 11.56-5.11 14.09-6.88s2.5-2.35.02-2.67z"/><path fill="#f4e7b1" d="M324.83 139.85c-1.09.73-3.88 2.42-3.89 3.26s4.73.47 6.18.07c0 0-4.16.44-5.11-.31-.71-.57 2.82-3.02 2.82-3.02z"/><path fill="#ecd26a" d="M328.2 138.58a19.89 19.89 0 00-2.18 1.33c-1 .71-2.12 1.59-1.45 2.06s2.16.41 4.81-.07 6.76-1.63 6.76-1.63-5.8 1.92-8.31 2.36-4.45.29-4.7-.37c-.3-.82 2.42-2.78 5-3.92z"/><path fill="#7e9acc" d="M483.7 148.15a7.1 7.1 0 11-8.57-5.22 7.1 7.1 0 018.57 5.22z"/><g fill="#d3e8f7" opacity=".5"><path d="M475 145.87c-.5-.57-1.33-1.42-2-2.07a7.25 7.25 0 00-1.08.81c1.15 1 2.25 2 2.56 2.33s1.52-.04.52-1.07zM483 153.28c-1.45-.85-4.14-2.44-5.28-3.18-1.61-1-2.84-.78-3.32-1.19s-2.24-2.21-3.34-3.24a7.15 7.15 0 00-.44.68c.88 1 2.3 2.53 2.61 2.84.46.47.28 1.16-.27.67-.34-.31-1.82-1.46-2.88-2.29a7.42 7.42 0 00-.33 1.5c1.59 1.43 3.54 2.77 4.14 2.83s1.4-1.22 2.22-.77c.61.34 4.09 2.54 5.8 3.61a6.78 6.78 0 001.09-1.46zM478.48 156.72a7.2 7.2 0 002.4-1.09c-1.38-.75-3.57-1.91-4.2-2.12-.93-.33-.83 1.31-1.58 1.35s-2.88-1.47-5.2-3.43v.07a7.1 7.1 0 008.58 5.22zM478.09 142.85c.06.38.32.78 1 1.36 1.1.9 2 1.48 2.37 1.87s-.65.54-.12 1.18a14.76 14.76 0 002.49 1.79c0-.3-.09-.6-.16-.9a7.09 7.09 0 00-5.58-5.3zM478 146.94c-.46-.67.26-1.39-.28-2.17a23.91 23.91 0 00-1.74-2 6.67 6.67 0 00-1.64.4 23.8 23.8 0 012.12 2.59c.28.54-.58 1.42-.17 1.73s5.54 3.63 7.24 4.73a7.16 7.16 0 00.37-1.6c-1.51-.81-5.57-3.14-5.9-3.68z"/></g><path fill="#5f71ae" d="M483.13 146.6a7.07 7.07 0 00-3.68-3.36 7.93 7.93 0 010 7.15c-1.85 4-6.73 5-6.95 5.06a7.1 7.1 0 0010.66-8.85z" opacity=".5"/><path fill="#5f71ae" d="M482.61 146.72a6.6 6.6 0 01-8.95 8.84 7 7 0 007.84-10 7.89 7.89 0 00-.6-1 6.61 6.61 0 011.71 2.16z"/><path fill="#d3e8f7" d="M477.71 143.65a6 6 0 00-6 2.91 6.59 6.59 0 00.79 7.68 8.12 8.12 0 01.11-6.4 8.71 8.71 0 015.1-4.19z" opacity=".7"/><path fill="#d3e8f7" d="M477.71 143.65s-4.1-.22-5.87 3.25a7.35 7.35 0 00.67 7.34s-3.28-3.37-1.08-7.55a6 6 0 016.28-3.04z"/><circle cx="304.62" cy="187.81" r="7.09" fill="#7e9acc" transform="rotate(-71.27 304.65 187.81)"/><g fill="#d3e8f7" opacity=".5"><path d="M302.86 183.85c-.51-.56-1.33-1.41-2-2.07a7.22 7.22 0 00-1.07.82c1.15 1.05 2.24 2 2.55 2.33s1.44-.04.52-1.08zM310.81 191.27c-1.44-.85-4.13-2.44-5.28-3.18-1.61-1-2.83-.78-3.32-1.19s-2.24-2.21-3.34-3.24a6 6 0 00-.43.68c.88 1 2.29 2.53 2.6 2.84.46.47.28 1.16-.27.67-.34-.31-1.81-1.46-2.87-2.29a6.27 6.27 0 00-.33 1.5c1.58 1.43 3.54 2.76 4.13 2.82s1.41-1.21 2.22-.76c.61.34 4.1 2.54 5.81 3.61a7 7 0 001.08-1.46zM306.3 194.7a7.07 7.07 0 002.4-1.08c-1.39-.75-3.58-1.91-4.2-2.13-.93-.32-.84 1.31-1.58 1.36s-2.89-1.47-5.21-3.43a.64.64 0 000 .07 7.09 7.09 0 008.59 5.21zM305.9 180.84c.06.38.33.78 1 1.35 1.1.91 2 1.49 2.37 1.88s-.65.54-.11 1.18a14.65 14.65 0 002.48 1.78 5.87 5.87 0 00-.16-.9 7.08 7.08 0 00-5.58-5.29zM305.76 184.93c-.46-.67.27-1.4-.27-2.17a25.6 25.6 0 00-1.74-2l-.81.15a7.46 7.46 0 00-.84.26 24.47 24.47 0 012.13 2.59c.28.54-.59 1.41-.17 1.73s5.54 3.63 7.23 4.73a6.75 6.75 0 00.38-1.61c-1.46-.81-5.53-3.14-5.91-3.68z"/></g><path fill="#5f71ae" d="M310.94 184.59a7.07 7.07 0 00-3.67-3.37 8 8 0 010 7.15c-1.86 4-6.74 5-7 5.06a7.1 7.1 0 0010.66-8.84z" opacity=".5"/><path fill="#5f71ae" d="M310.42 184.71a6.6 6.6 0 01-8.94 8.84 7 7 0 007.83-10 6.78 6.78 0 00-.59-1 6.58 6.58 0 011.7 2.16z"/><path fill="#d3e8f7" d="M305.52 181.64a6 6 0 00-6 2.91 6.56 6.56 0 00.79 7.68 8.08 8.08 0 01.11-6.4 8.65 8.65 0 015.1-4.19z" opacity=".7"/><path fill="#d3e8f7" d="M305.52 181.64s-4.09-.23-5.86 3.25a7.33 7.33 0 00.67 7.34s-3.29-3.37-1.08-7.55a5.93 5.93 0 016.27-3.04z"/><circle cx="476.81" cy="149.82" r="9.43" fill="none" stroke="#5c4f84" stroke-miterlimit="10" stroke-width=".798"/><circle cx="476.81" cy="149.82" r="14.36" fill="none" stroke="#514575" stroke-dasharray="2.255 2.255 0 2.255 2.255 0" stroke-linecap="round" stroke-miterlimit="10" stroke-width="1.102"/><circle cx="338.06" cy="135.84" r="21.74" fill="none" stroke="#514575" stroke-dasharray="3.414 3.414 0 3.414 3.414 0" stroke-linecap="round" stroke-miterlimit="10" stroke-width="1.102" transform="rotate(-31.72 338.036 135.845)"/><path fill="none" stroke="#5c5381" stroke-miterlimit="10" stroke-width=".735" d="M534.73 238.5l6.29-3.83M520.2 227.9l14.53 10.6 6.18 7.56 7.03-1.19M527.99 207.14l11.3 13.18 1.73 14.35 5.86 3.5 1.06 6.7 16.49 5.09 15.32.32"/><path fill="#f3eece" d="M526.71 207.14a1.28 1.28 0 111.28 1.28 1.27 1.27 0 01-1.28-1.28z"/><circle cx="539.29" cy="220.32" r="1.41" fill="#f3eece"/><path fill="#f3eece" d="M519.34 227.9a.87.87 0 11.86.86.86.86 0 01-.86-.86zM533.59 238.5a1.14 1.14 0 111.14 1.14 1.14 1.14 0 01-1.14-1.14zM540.16 234.67a.86.86 0 11.86.86.85.85 0 01-.86-.86zM563.57 250a.86.86 0 11.86.86.86.86 0 01-.86-.86z"/><circle cx="546.88" cy="238.17" r=".65" fill="#f3eece"/><path fill="#f3eece" d="M540.26 246.06a.65.65 0 111.3 0 .65.65 0 11-1.3 0zM547 244.87a1 1 0 111 1 1 1 0 01-1-1z"/><circle cx="579.75" cy="250.28" r="1.08" fill="#f3eece"/><ellipse cx="418.58" cy="322.91" fill="#504382" rx="62.46" ry="25.6"/><path fill="#6a4f7c" d="M351.38 301.11a28.72 28.72 0 0157.42 0 7.22 7.22 0 010 .8 7.31 7.31 0 010 .81c-.32 4-3.12 7.87-8.4 10.93-11.21 6.47-29.41 6.47-40.64 0-5.26-3.06-8.06-7-8.38-10.93a7.31 7.31 0 010-.81 7.22 7.22 0 010-.8z"/><path fill="#855c75" d="M367.63 276.05a28.68 28.68 0 0141.17 25.06 7.22 7.22 0 010 .8 7.31 7.31 0 010 .81c-.32 4-3.12 7.87-8.4 10.93a38.26 38.26 0 01-14.4 4.49c7.45-1.28 12.27-9.6 10-18.79-2.69-10.66-13.46-26.06-28.37-23.3z"/><path fill="#5a477d" d="M351.38 302.72a7.31 7.31 0 010-.81 7.22 7.22 0 010-.8 28.54 28.54 0 019.75-20.75c-3.12 3.21-10.06 15.3-2.52 24.52 5 6.06 28.51 14.71 47.88 3.59a20.06 20.06 0 01-6.09 5.18c-11.21 6.47-29.41 6.47-40.64 0-5.26-3.06-8.06-6.96-8.38-10.93z"/><path fill="#a1727c" d="M380.38 279.65c-1.28 2.93 1.19 6.85 5.52 8.75s8.89 1.07 10.17-1.86-1.18-6.84-5.51-8.74-8.89-1.08-10.18 1.85z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#926279" d="M397 291.57c-.67 1.52.3 3.43 2.17 4.25s3.93.25 4.6-1.28-.3-3.42-2.17-4.25-3.91-.29-4.6 1.28z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#443b6c" d="M400.4 313.65c-11.21 6.47-29.41 6.47-40.64 0a20.06 20.06 0 01-6.07-5.17c.06.06 8.91 8.65 26.35 8.65s26.45-8.66 26.45-8.66a20.06 20.06 0 01-6.09 5.18z"/><path fill="#6a4f7c" d="M485.83 306.43a26 26 0 00-51.93 0v1.45c.29 3.59 2.83 7.12 7.6 9.88 10.13 5.86 26.59 5.86 36.75 0 4.75-2.76 7.28-6.29 7.58-9.88v-.72c0-.24.02-.48 0-.73z"/><path fill="#855c75" d="M471.13 283.76a25.94 25.94 0 00-37.23 22.67v1.45c.29 3.59 2.83 7.12 7.6 9.88a34.6 34.6 0 0013 4.07c-6.74-1.16-11.1-8.69-9-17 2.41-9.63 12.15-23.56 25.63-21.07z"/><path fill="#5a477d" d="M485.83 307.88v-.72-.73a25.89 25.89 0 00-8.83-18.77c2.82 2.9 9.1 13.84 2.28 22.17-4.49 5.49-25.78 13.31-43.3 3.26a18 18 0 005.51 4.67c10.13 5.86 26.59 5.86 36.75 0 4.76-2.76 7.29-6.29 7.59-9.88z"/><path fill="#a1727c" d="M459.6 287c1.16 2.65-1.07 6.19-5 7.91s-8 1-9.2-1.67 1.07-6.19 5-7.91 8.04-.95 9.2 1.67z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#926279" d="M444.55 297.8c.61 1.38-.27 3.1-2 3.84s-3.55.23-4.16-1.15.28-3.1 2-3.84 3.61-.23 4.16 1.15z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#443b6c" d="M441.5 317.76c10.13 5.86 26.59 5.86 36.75 0a18.24 18.24 0 005.49-4.67c-.06.06-8.07 7.82-23.83 7.82S436 313.09 436 313.09a18 18 0 005.5 4.67z"/><path fill="#73537b" d="M490.72 323.79a21.15 21.15 0 00-42.29 0 8.71 8.71 0 000 1.18c.24 2.93 2.31 5.8 6.19 8 8.25 4.77 21.66 4.77 29.93 0 3.86-2.25 5.93-5.12 6.17-8a8.71 8.71 0 000-1.18z"/><path fill="#996664" d="M478.75 305.33a21.12 21.12 0 00-30.32 18.46 8.71 8.71 0 000 1.18c.24 2.93 2.31 5.8 6.19 8a28.23 28.23 0 0010.61 3.31c-5.48-.95-9-7.07-7.35-13.84 1.96-7.79 9.89-19.14 20.87-17.11z" style="mix-blend-mode:lighten"/><path fill="#624b7d" d="M490.72 325a8.71 8.71 0 000-1.18 21 21 0 00-7.18-15.28c2.3 2.36 7.41 11.26 1.85 18.05-3.65 4.47-21 10.84-35.26 2.65a14.93 14.93 0 004.49 3.81c8.25 4.77 21.66 4.77 29.93 0 3.86-2.28 5.93-5.15 6.17-8.05z"/><path fill="#cca084" d="M469.36 308c.95 2.15-.87 5-4.06 6.44s-6.55.79-7.49-1.37.87-5 4.06-6.44 6.54-.8 7.49 1.37zM457.11 316.76a2.78 2.78 0 11-3.39-.94 2.51 2.51 0 013.39.94z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#4f3c68" d="M454.62 333c8.25 4.77 21.66 4.77 29.93 0a14.69 14.69 0 004.47-3.81c0 .05-6.57 6.37-19.41 6.37s-19.48-6.37-19.48-6.37a14.93 14.93 0 004.49 3.81z"/><path fill="#624b7c" d="M528.9 322.39a21.18 21.18 0 00-42.34 0v.59a5.72 5.72 0 000 .59c.24 2.94 2.3 5.81 6.2 8.06 8.26 4.78 21.69 4.78 30 0 3.87-2.25 5.94-5.12 6.17-8.06a5.72 5.72 0 000-.59c-.01-.2-.01-.38-.03-.59z"/><path fill="#855c75" d="M516.92 303.91a21 21 0 00-9.19-2.12 21.18 21.18 0 00-21.17 20.6v.59a5.72 5.72 0 000 .59c.24 2.94 2.3 5.81 6.2 8.06a28.11 28.11 0 0010.62 3.37c-5.49-.95-9.05-7.08-7.36-13.86 1.98-7.91 9.91-19.26 20.9-17.23z"/><path fill="#5a477d" d="M528.9 323.57a5.72 5.72 0 000-.59v-.59a21 21 0 00-7.18-15.3c2.3 2.36 7.41 11.28 1.85 18.08-3.66 4.47-21 10.85-35.31 2.65a14.72 14.72 0 004.5 3.81c8.26 4.78 21.69 4.78 30 0 3.84-2.25 5.91-5.12 6.14-8.06z"/><path fill="#a1727c" d="M507.52 306.57c.94 2.16-.88 5-4.07 6.45s-6.56.79-7.5-1.37.87-5 4.06-6.45 6.56-.79 7.51 1.37zM495.25 315.35a2.78 2.78 0 11-3.39-.94 2.53 2.53 0 013.39.94z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#4f3c68" d="M492.76 331.63c8.26 4.78 21.69 4.78 30 0a14.69 14.69 0 004.47-3.81c-.05.05-6.57 6.38-19.43 6.38s-19.51-6.38-19.51-6.38a14.72 14.72 0 004.47 3.81z"/><path fill="#bc7572" d="M443.93 294.13h-50.12a21.25 21.25 0 00-6.23 15V349h62.58v-39.84a21.25 21.25 0 00-6.23-15.03z"/><path fill="#e5bf7c" d="M410.78 297.31H427A16.71 16.71 0 01443.68 314v34.5h-49.62V314a16.71 16.71 0 0116.72-16.69z" style="mix-blend-mode:lighten"/><path fill="#f3eece" d="M416.11 300.62H421a13.17 13.17 0 0113.17 13.17V348h-31.23v-34.21a13.17 13.17 0 0113.17-13.17z"/><path fill="#d29b72" d="M443.79 293.43l-7.29-1.63-7.29 1.63a22.08 22.08 0 00.08 8.64c1 5.28 5.22 10.55 7.21 10.55s6.26-5.27 7.21-10.55a22.08 22.08 0 00.08-8.64z"/><path fill="#e8c275" d="M441.27 294.19h-10c-1.42 7.43 3.16 13.13 5 13.13s6.43-5.7 5-13.13z"/><path fill="#f3eece" d="M436.28 294.19H438a5.86 5.86 0 01.93 4c-.21 2-1.61 4.61-2.64 4.61s-2.43-2.61-2.63-4.61a5.89 5.89 0 01.92-4h1.71M433.3 302.55a.56.56 0 11.56.56.56.56 0 01-.56-.56zM435 304.94a1.24 1.24 0 112.48 0 1.24 1.24 0 01-2.48 0z"/><path fill="#b9787a" d="M441 290.08a3.47 3.47 0 001.87-3.15l-1.66-6.11-2.44 3.18.73 6.83a7.42 7.42 0 001.5-.75z"/><path fill="#e7bd88" d="M432 290.08a7.07 7.07 0 001.57.73l.73-6.84h-3.36l-.8 3a3.44 3.44 0 001.86 3.11z"/><path fill="#afa39a" d="M431.57 292.36a3.8 3.8 0 01-2-3.29l-.95 3.47a3.94 3.94 0 002.32 3.23 9.13 9.13 0 002 .84l.37-3.45a7.52 7.52 0 01-1.74-.8z"/><path fill="#806d60" d="M443.06 287.51l.08.29.34 1.28a3.82 3.82 0 01-2 3.28 7.71 7.71 0 01-1.69.79l.37 3.45a9.49 9.49 0 002-.83 3.92 3.92 0 002.32-3.23z"/><path fill="#675763" d="M442.9 286.93l.16.58-.16-.58zM430.11 286.93l-.24.87-.34 1.26.58-2.13z"/><path fill="#604242" d="M441 290.08a7.42 7.42 0 01-1.53.72l.25 2.35a7.71 7.71 0 001.69-.79 3.82 3.82 0 002-3.28l-.34-1.28-.08-.29-.16-.58a3.47 3.47 0 01-1.83 3.15z"/><path fill="#776471" d="M431.57 292.36a7.52 7.52 0 001.72.8l.25-2.35a7.07 7.07 0 01-1.57-.73 3.44 3.44 0 01-1.86-3.15l-.58 2.14a3.8 3.8 0 002.04 3.29z"/><path fill="#dd9f71" d="M439.5 290.8l-.73-6.83h-4.5l-.73 6.84a9.63 9.63 0 005.96-.01z"/><path fill="#917e6e" d="M433.29 293.16l-.37 3.45a13.24 13.24 0 007.2 0l-.37-3.45a10.48 10.48 0 01-6.46 0z"/><path fill="#675763" d="M433.54 290.81l-.25 2.35a10.48 10.48 0 006.46 0l-.25-2.35a9.63 9.63 0 01-5.96 0z"/><path fill="#e7bd88" d="M432.27 284h-1.36l-.8 3-.58 2.14-.95 3.47a3.94 3.94 0 002.32 3.23 9.13 9.13 0 002 .84 11.51 11.51 0 001.69.36.41.41 0 00.51-.36.62.62 0 00-.49-.53c-3.15-.83-4.69-2.72-4.52-3.45s1.77-7.11 2.18-8.7zM436.12 296.68c0-.24.29-.44.62-.45s.6.17.61.41-.26.46-.61.46-.62-.19-.62-.42z" style="mix-blend-mode:soft-light"/><path fill="#675763" d="M442.11 284l-.87-3.2-2.47 3.2h-7.86l-.8 3-.24.87-.34 1.27-.66 2.41c5.87-1.55 10.61-4.19 13.24-7.55z" opacity=".2" style="mix-blend-mode:multiply"/><path fill="#d29b72" d="M408.52 293.43l-7.29-1.63-7.29 1.63a22.08 22.08 0 00.08 8.64c1 5.28 5.22 10.55 7.21 10.55s6.26-5.27 7.21-10.55a21.84 21.84 0 00.08-8.64z"/><path fill="#e8c275" d="M406 294.19h-10c-1.42 7.43 3.16 13.13 5 13.13s6.43-5.7 5-13.13z"/><path fill="#f3eece" d="M401 294.19h1.71a5.86 5.86 0 01.93 4c-.21 2-1.61 4.61-2.64 4.61s-2.43-2.61-2.63-4.61a5.86 5.86 0 01.93-4h1.7M398 302.55a.56.56 0 11.56.56.56.56 0 01-.56-.56zM399.77 304.94a1.24 1.24 0 012.48 0 1.24 1.24 0 11-2.48 0z"/><path fill="#b9787a" d="M405.76 290.08a3.47 3.47 0 001.87-3.15l-1.63-6.11-2.5 3.18.73 6.83a7.42 7.42 0 001.53-.75z"/><path fill="#e7bd88" d="M396.7 290.08a7.07 7.07 0 001.57.73L399 284l-2.47-3.15-1.69 6.11a3.44 3.44 0 001.86 3.12z"/><path fill="#afa39a" d="M396.3 292.36a3.8 3.8 0 01-2-3.29l-.95 3.47a3.94 3.94 0 002.32 3.23 9.13 9.13 0 002 .84l.37-3.45a7.52 7.52 0 01-1.74-.8z"/><path fill="#806d60" d="M407.79 287.51l.08.29.34 1.28a3.82 3.82 0 01-2 3.28 7.71 7.71 0 01-1.69.79l.37 3.45a9.49 9.49 0 002-.83 3.92 3.92 0 002.32-3.23z"/><path fill="#675763" d="M407.63 286.93l.16.58-.16-.58zM394.84 286.93l-.24.87-.34 1.26.58-2.13z"/><path fill="#604242" d="M405.76 290.08a7.42 7.42 0 01-1.53.72l.25 2.35a7.71 7.71 0 001.69-.79 3.82 3.82 0 002-3.28l-.34-1.28-.08-.29-.16-.58a3.47 3.47 0 01-1.83 3.15z"/><path fill="#776471" d="M396.3 292.36a7.52 7.52 0 001.72.8l.25-2.35a7.07 7.07 0 01-1.57-.73 3.44 3.44 0 01-1.86-3.15l-.58 2.14a3.8 3.8 0 002.04 3.29z"/><path fill="#dd9f71" d="M404.23 290.8l-.73-6.8H399l-.73 6.84a9.63 9.63 0 005.96-.04z"/><path fill="#917e6e" d="M398 293.16l-.37 3.45a13.24 13.24 0 007.2 0l-.37-3.45a10.48 10.48 0 01-6.46 0z"/><path fill="#675763" d="M398.27 290.81l-.25 2.35a10.48 10.48 0 006.46 0l-.25-2.35a9.63 9.63 0 01-5.96 0z"/><path fill="#e7bd88" d="M397.52 282l-1-1.21-1.69 6.11-.58 2.14-.95 3.47a3.94 3.94 0 002.32 3.23 9.13 9.13 0 002 .84 11.37 11.37 0 001.7.36.41.41 0 00.5-.36.62.62 0 00-.49-.53c-3.15-.83-4.69-2.72-4.52-3.45s2.3-8.94 2.71-10.6zM400.86 296.68c0-.24.28-.44.61-.45a.53.53 0 01.61.41c0 .24-.26.46-.61.46s-.62-.19-.61-.42z" style="mix-blend-mode:soft-light"/><path fill="#675763" d="M396.53 280.82l-.88 3.17c2.62 3.35 7.34 6 13.21 7.48l-1.07-4-.16-.58-1.63-6.07-2.5 3.18H399l-1.49-1.9z" opacity=".2" style="mix-blend-mode:multiply"/><path fill="#d29b72" d="M428.59 299.61l-9.72-2.18-9.72 2.18a29.16 29.16 0 00.11 11.52c1.27 7 6.95 14.07 9.61 14.07s8.34-7 9.61-14.07a29.4 29.4 0 00.11-11.52z"/><path fill="#e8c275" d="M425.23 300.62h-13.31c-1.9 9.91 4.21 17.51 6.66 17.51s8.55-7.6 6.65-17.51z"/><path fill="#f3eece" d="M418.58 300.62h2.28a7.77 7.77 0 011.23 5.29c-.27 2.67-2.14 6.15-3.51 6.15s-3.24-3.48-3.52-6.15a7.81 7.81 0 011.24-5.29h2.28M414.6 311.77a.75.75 0 11.75.75.76.76 0 01-.75-.75zM416.92 315a1.66 1.66 0 111.66 1.65 1.66 1.66 0 01-1.66-1.65z"/><path fill="#b9787a" d="M424.91 294.43c1.8-1.15 2.63-2.69 2.49-4.2l-1.07-4h-4.44l1 9.12a9.34 9.34 0 002.02-.92z"/><path fill="#e7bd88" d="M412.83 294.43a9.47 9.47 0 002.08 1l1-9.13h-4.48l-1.07 4c-.16 1.44.64 2.98 2.47 4.13z"/><path fill="#afa39a" d="M412.29 297.47c-1.89-1.21-2.8-2.8-2.72-4.39l-1.26 4.63c0 1.56 1 3.12 3.09 4.31a12 12 0 002.69 1.12l.49-4.59a10.25 10.25 0 01-2.29-1.08z"/><path fill="#806d60" d="M427.61 291l.1.39.46 1.7a5.08 5.08 0 01-2.72 4.37 9.89 9.89 0 01-2.25 1.06l.49 4.6a12 12 0 002.64-1.11c2.06-1.19 3.09-2.75 3.09-4.31z"/><path fill="#675763" d="M427.4 290.23l.21.78-.21-.78zM410.34 290.23l-.32 1.17-.46 1.68.78-2.85z"/><path fill="#604242" d="M424.91 294.43a9.34 9.34 0 01-2 1l.33 3.13a9.89 9.89 0 002.25-1.06 5.08 5.08 0 002.72-4.37l-.46-1.7-.1-.39-.21-.78c.1 1.48-.73 3.02-2.53 4.17z"/><path fill="#776471" d="M412.29 297.47a10.25 10.25 0 002.29 1.08l.33-3.14a9.47 9.47 0 01-2.08-1c-1.8-1.15-2.63-2.69-2.49-4.2l-.77 2.85c-.08 1.61.83 3.2 2.72 4.41z"/><path fill="#dd9f71" d="M422.87 295.4l-1-9.12h-6l-1 9.13a13 13 0 008-.01z"/><path fill="#917e6e" d="M414.58 298.55l-.49 4.59a17.59 17.59 0 009.6 0l-.49-4.6a14.1 14.1 0 01-8.62.01z"/><path fill="#675763" d="M414.91 295.41l-.33 3.14a14.1 14.1 0 008.62 0l-.33-3.13a13 13 0 01-7.96-.01z"/><path fill="#e7bd88" d="M413.22 286.28h-1.81l-1.07 4-.77 2.85-1.26 4.63c0 1.56 1 3.12 3.09 4.31a12 12 0 002.69 1.12 15.37 15.37 0 002.26.48.55.55 0 00.68-.48.85.85 0 00-.67-.71c-4.19-1.1-6.24-3.63-6-4.6s2.32-9.43 2.86-11.6zM418.36 303.23a.8.8 0 01.82-.6.72.72 0 01.82.55c0 .32-.35.61-.82.62s-.83-.26-.82-.57z" style="mix-blend-mode:soft-light"/><path fill="#675763" d="M418.85 292.65a43.29 43.29 0 008.95-.91l-.09-.34-.1-.39-.21-.78-1.07-4h-14.92l-1.07 4-.41 1.52a43.71 43.71 0 008.92.9z" opacity=".2" style="mix-blend-mode:multiply"/><path fill="#d68d97" d="M444.2 249.64V276.42c0 .15-.05.3-.08.44a1.89 1.89 0 01-.05.23c0 .17-.08.33-.13.49a10.44 10.44 0 01-.37 1l-.1.23c-.07.15-.14.3-.22.45a.9.9 0 01-.05.09 10.22 10.22 0 01-1.11 1.72l-.46.57c-.25.28-.51.56-.78.83l-.72.66-.17.15c-.25.22-.52.43-.8.64l-.2.16c-.26.19-.53.37-.8.55l-.21.14a6 6 0 01-.53.34c-.17.12-.36.23-.55.34-.34.19-.7.39-1.06.57h-.06c-.35.19-.71.36-1.08.52l-1 .45-.36.15-.91.34h-.1l-1.3.52c-9.63 3-21.94 2.2-30.09-2.5-4.95-2.86-7.43-6.61-7.43-10.35v-25.5z"/><path fill="#d28088" d="M418.89 283.11c0 3.68-3.27 6.24-12.68 4.72a42 42 0 0025.36 0V262.3l-12.68 2z"/><path fill="#e1afb9" d="M406.21 249.65H393.5v25.48c0 3.75 2.48 7.5 7.43 10.36a29 29 0 005.28 2.34z"/><path fill="#eacbd2" d="M396.53 271.93c0 2.92 1.49 6.14 3.33 7.2s3.32-.44 3.32-3.36v-21.86l-6.65-3.85z"/><path fill="#ce757a" d="M436.8 260a28.45 28.45 0 01-5.23 2.3v18.57c0 3.72-10.35 9.47-21.67 7.95 9 2 19.63.87 26.9-3.33.38-.22.74-.45 1.09-.67v-25.49c-.35.23-.71.45-1.09.67z"/><path fill="#c7686c" d="M444.2 250.3V276.42c0 .15-.05.3-.08.44a1.89 1.89 0 01-.05.23c0 .17-.08.33-.13.49a10.44 10.44 0 01-.37 1l-.1.23c-.07.15-.14.3-.22.45a.9.9 0 01-.05.09 11.65 11.65 0 01-1.11 1.72l-.46.57a17.58 17.58 0 01-3.68 3.13 6 6 0 01-.53.34c-.17.12-.36.23-.55.34-.34.19-.7.39-1.06.57h-.06c-.35.19-.71.36-1.08.52l-1 .45-.36.15-.91.34h-.1l-1.3.52a39.59 39.59 0 01-3.86 1c9.28-3.12 10.74-8.3 10.74-12.23v-17.4c3.96-2.63 6.12-5.83 6.32-9.07z"/><path fill="#a8c0e3" d="M393.5 239.78v9.87c0 3.74 2.48 7.49 7.43 10.35a29 29 0 005.28 2.32v-22.54z"/><path fill="#d3e8f7" d="M403.18 239.78h-6.65v16.8a18.91 18.91 0 004.4 3.42c.72.41 1.48.79 2.25 1.14z"/><path fill="#7e9acc" d="M406.21 239.78v22.54a42 42 0 0025.36 0v-22.54z"/><path fill="#7591c5" d="M418.89 264.27a40.41 40.41 0 0012.68-2v-22.49h-12.68z"/><path fill="#6c85bd" d="M437.89 259.33v-9.68h-.28l-.81.49a29.14 29.14 0 01-5.23 2.3v9.86a28.45 28.45 0 005.23-2.3c.38-.22.74-.44 1.09-.67z"/><path fill="#5f71ae" d="M437.89 249.46v9.87c4-2.59 6.06-5.79 6.31-9v-9.86c-.2 3.21-2.35 6.41-6.31 8.99z"/><path fill="#d3e8f7" d="M393.5 229.92v9.86c0 3.75 2.48 7.5 7.43 10.36a29 29 0 005.28 2.31v-22.53z"/><path fill="#f1f8fc" d="M403.18 229.92h-6.65v16.8a19.18 19.18 0 004.4 3.42c.72.41 1.48.78 2.25 1.13z"/><path fill="#a8c0e3" d="M406.21 229.92v22.53a42 42 0 0025.36 0v-22.53z"/><path fill="#9eb7dd" d="M418.89 254.41a40.41 40.41 0 0012.68-2v-22.49h-12.68z"/><path fill="#7e9acc" d="M437.61 239.78c-.26.17-.53.33-.81.49a28.16 28.16 0 01-5.23 2.3v9.87a29.14 29.14 0 005.23-2.3l.81-.49.28-.19v-9.68z"/><path fill="#6c85bd" d="M437.89 239.6v9.86c4-2.58 6.06-5.78 6.31-9v-9.87c-.2 3.22-2.35 6.41-6.31 9.01z"/><path fill="#a8c0e3" d="M393.5 220.05v9.87c0 3.74 2.48 7.49 7.43 10.35a29 29 0 005.28 2.32v-22.54z"/><path fill="#d3e8f7" d="M403.18 220.05h-6.65v16.8a18.91 18.91 0 004.4 3.42c.72.41 1.48.79 2.25 1.14z"/><path fill="#7e9acc" d="M406.21 220.05v22.54a42 42 0 0025.36 0v-22.54z"/><path fill="#7591c5" d="M418.89 244.54a40.41 40.41 0 0012.68-2v-22.49h-12.68z"/><path fill="#6c85bd" d="M437.61 229.92l-.81.49a29.19 29.19 0 01-5.23 2.32v9.84a28.16 28.16 0 005.23-2.3c.28-.16.55-.32.81-.49l.28-.18v-9.86z"/><path fill="#5f71ae" d="M444.2 220.05c0 3.45-2.09 6.9-6.31 9.67v9.86c4-2.59 6.06-5.79 6.31-9v-10.53z"/><path fill="#f5e5c2" d="M393.5 137.83v82.22c0 3.75 2.48 7.5 7.43 10.36a28.34 28.34 0 005.28 2.33v-82.23z"/><path fill="#fcf7ed" d="M403.18 147.5l-6.65-6.65V227a18.91 18.91 0 004.4 3.42c.72.41 1.48.79 2.25 1.14z"/><path fill="#dea177" d="M431.57 150.51v82.22a29.19 29.19 0 005.23-2.32c4.95-2.86 7.43-6.61 7.4-10.34v-82.24z"/><path fill="#edcf8e" d="M431.57 150.51v82.22l-.2.07a40.12 40.12 0 01-11 1.87h-3a40.13 40.13 0 01-10.91-1.84 1.84 1.84 0 01-.25-.09v-82.23z"/><path fill="#e9c488" d="M425.22 158.85a6.35 6.35 0 00-6.35 6.35v39.1a6.35 6.35 0 006.35 6.36 6.35 6.35 0 006.35-6.36v-39.1a6.35 6.35 0 00-6.35-6.35zM425.22 217.79a6.35 6.35 0 00-6.35 6.35v.24a6.35 6.35 0 006.35 6.35 6.35 6.35 0 006.35-6.35v-.24a6.35 6.35 0 00-6.35-6.35z"/><path fill="#ce8a74" d="M437.89 144.19v85.55c4.22-2.77 6.34-6.22 6.31-9.67v-82.21z"/><path fill="#7e9acc" d="M418.87 225.74a5.52 5.52 0 01-5.52-5.52v-8.31a5.52 5.52 0 015.52-5.52 5.52 5.52 0 015.51 5.52v8.31a5.52 5.52 0 01-5.51 5.52z"/><path fill="#7591c5" d="M424.38 220.22v-8.31a5.52 5.52 0 00-5.51-5.52v19.35a5.52 5.52 0 005.51-5.52z"/><text fill="#fcf7ed" font-family="AsapCondensed-SemiBold,Asap Condensed" font-size="15.5" font-weight="600" transform="translate(415.31 221.62)">2</text><path fill="#5f71ae" d="M463 276.22v29.46a1.65 1.65 0 01-1.64 1.64 1.73 1.73 0 01-1.72-1.55v-.09c0-1.45-.15-2.88-.32-4.31-.06-.47-.12-.95-.19-1.42s-.11-.67-.17-1-.06-.41-.1-.62c-.07-.36-.13-.72-.21-1.08a.53.53 0 000-.12c-.07-.39-.16-.79-.25-1.17 0-.15-.07-.28-.1-.42s-.1-.44-.16-.66-.17-.68-.27-1a3 3 0 00-.09-.32c-.12-.44-.25-.87-.39-1.31l-.33-1c-.09-.25-.17-.5-.27-.75s-.26-.72-.39-1.07-.29-.76-.45-1.13c-.41-1-.86-2-1.35-3-.22-.45-.45-.9-.68-1.35s-.48-.9-.72-1.33c-.5-.87-1-1.73-1.56-2.58s-1.12-1.69-1.72-2.5c-.89-1.22-1.85-2.41-2.85-3.55a50.6 50.6 0 00-9.17-8.14c-4.59-9.37-3.82-19.64 0-30.44a45.85 45.85 0 0125.1 40.81z"/><path fill="#4f5ea1" d="M461.37 276c-.65.83-1.39-.63-2-3.46L454 284a49.46 49.46 0 011.97 4.22c.16.37.31.75.45 1.13s.27.71.39 1.07.18.5.27.75l.33 1c.14.44.27.87.39 1.31a3 3 0 01.09.32c.1.33.19.67.27 1s.11.44.16.66.07.27.1.42c.09.38.18.78.25 1.17a.53.53 0 010 .12c.08.36.14.72.21 1.08 0 .21.08.41.1.62s.12.68.17 1 .13.95.19 1.42c.17 1.43.28 2.86.32 4.31v.09a1.73 1.73 0 001.72 1.55 1.65 1.65 0 001.64-1.64v-29.38a46.25 46.25 0 00-1-9.52c.67 3.8.25 8.18-.65 9.3z"/><path fill="#697eb8" d="M461.37 298.11v9.21a1.73 1.73 0 01-1.72-1.55v-.09c0-1.45-.16-2.89-.32-4.31-.06-.47-.13-.95-.19-1.42s-.11-.67-.17-1-.06-.41-.1-.62c-.07-.36-.13-.72-.21-1.08a.53.53 0 000-.12c-.07-.39-.16-.79-.25-1.17 0-.15-.07-.28-.1-.42s-.1-.44-.16-.66-.17-.68-.27-1a3 3 0 00-.09-.32c-.12-.44-.25-.88-.39-1.31s-.22-.7-.33-1-.17-.5-.27-.75-.26-.72-.39-1.07-.29-.76-.45-1.13c-.41-1-.86-2-1.35-3-.22-.45-.44-.9-.68-1.35s-.48-.9-.72-1.33q-.75-1.32-1.56-2.58c-.55-.86-1.12-1.69-1.72-2.5a53.97 53.97 0 00-2.85-3.55 50.6 50.6 0 00-9.17-8.14c-4.59-9.37-3.82-19.64 0-30.44 9.48 9.86 23.46 24.33 23.46 62.7z"/><path fill="#a8c0e3" d="M461.37 298.11s-.08-1.07-.2-3c-.05-.95-.12-2.09-.2-3.41s-.29-2.78-.42-4.38c-.08-.81-.16-1.64-.25-2.51s-.25-1.75-.38-2.66-.27-1.85-.41-2.81-.36-1.93-.54-2.92-.38-2-.6-3-.5-2-.76-3c-.12-.52-.25-1-.37-1.55s-.31-1-.47-1.52c-.32-1-.63-2-.95-3.07-.76-2-1.42-4-2.33-5.94s-1.77-3.77-2.69-5.56l-1.49-2.55c-.47-.85-1-1.61-1.51-2.39-.26-.39-.49-.78-.75-1.14s-.52-.72-.78-1.07c-.5-.71-1-1.41-1.48-2l-1.42-1.83-1.32-1.62c-.82-1-1.6-1.87-2.21-2.59l-1.94-2.25.56.54c.36.35.91.85 1.58 1.53s1.49 1.47 2.39 2.43c.45.48.93 1 1.44 1.53l1.53 1.77c.55.6 1.05 1.29 1.6 2s1.11 1.41 1.63 2.18 1.12 1.53 1.63 2.37l1.58 2.56c1 1.8 2 3.64 2.85 5.62s1.63 4 2.42 6c.31 1 .63 2.08.94 3.12.15.52.32 1 .46 1.56s.25 1 .37 1.56c.25 1.05.49 2.08.73 3.1s.35 2.06.53 3.06.36 2 .47 3 .21 1.93.31 2.85.19 1.83.28 2.71.08 1.72.12 2.53c.07 1.63.16 3.12.16 4.43s0 2.47-.05 3.41c-.02 1.8-.06 2.91-.06 2.91z"/><path fill="#5f71ae" d="M442.9 264.27c-4.72-4.38-8.07-14.48-7.86-17.37a32.73 32.73 0 002.84 18.85 50.54 50.54 0 0121.8 41.57c.14-27.93-12.16-38.76-16.78-43.05z"/><path fill="#7e9acc" d="M438.36 239.6c-1.57 2.36-.73 12.72 2.38 17.35s8.57 9.15 12.16 15c2.67 4.35 4.1 1.34 2.69-3.19s-3.18-11.68-7.85-18.88-8.74-11.17-9.38-10.28z" opacity=".7"/><path fill="#9eb7dd" d="M440.48 242c-1.24-1-1.11 3.2-.47 5.59s8.39 11.25 9.21 11.77.42-2.77-2.31-7.83c-2.54-4.75-4.59-8.04-6.43-9.53z" opacity=".5"/><path fill="#5f71ae" d="M374.72 276.22v29.46a1.65 1.65 0 001.64 1.64 1.72 1.72 0 001.72-1.55.28.28 0 010-.09c0-1.45.15-2.88.32-4.31 0-.47.11-.95.19-1.42s.1-.67.16-1 .06-.41.1-.62l.21-1.08v-.12c.07-.39.16-.79.26-1.17 0-.15.06-.28.09-.42s.1-.44.17-.66.17-.68.26-1l.09-.32c.12-.44.25-.87.39-1.31s.22-.7.34-1 .17-.5.26-.75.26-.72.39-1.07.29-.76.45-1.13c.41-1 .86-2 1.35-3 .22-.45.45-.9.68-1.35s.48-.9.72-1.33c.5-.87 1-1.73 1.57-2.58s1.12-1.69 1.71-2.5c.89-1.22 1.85-2.41 2.86-3.55a50.21 50.21 0 019.16-8.14c4.59-9.37 3.82-19.64 0-30.44a45.85 45.85 0 00-25.09 40.81z"/><path fill="#4f5ea1" d="M376.36 276c.65.83 1.39-.63 2-3.46l5.37 11.4a49.46 49.46 0 00-1.97 4.22c-.16.37-.3.75-.45 1.13s-.27.71-.39 1.07-.18.5-.26.75-.23.69-.34 1-.27.87-.39 1.31l-.09.32c-.09.33-.18.67-.26 1s-.12.44-.17.66-.07.27-.09.42c-.1.38-.19.78-.26 1.17v.12l-.21 1.08c0 .21-.07.41-.1.62s-.12.68-.16 1-.14.95-.19 1.42c-.17 1.43-.28 2.86-.32 4.31a.28.28 0 000 .09 1.72 1.72 0 01-1.72 1.55 1.65 1.65 0 01-1.64-1.64v-29.32a46.25 46.25 0 011-9.52c-.72 3.8-.26 8.18.64 9.3z"/><path fill="#697eb8" d="M376.36 298.11v9.21a1.72 1.72 0 001.72-1.55.28.28 0 010-.09c0-1.45.15-2.89.32-4.31.06-.47.12-.95.19-1.42s.1-.67.16-1 .07-.41.1-.62l.21-1.08v-.12c.07-.39.16-.79.26-1.17 0-.15.06-.28.09-.42s.1-.44.17-.66.17-.68.26-1l.09-.32c.12-.44.25-.88.39-1.31s.22-.7.34-1 .17-.5.26-.75.26-.72.39-1.07.29-.76.45-1.13c.41-1 .86-2 1.35-3 .22-.45.45-.9.68-1.35s.48-.9.72-1.33c.51-.88 1-1.74 1.57-2.58s1.12-1.69 1.71-2.5c.9-1.22 1.85-2.41 2.86-3.55a50.21 50.21 0 019.16-8.14c4.59-9.37 3.82-19.64 0-30.44-9.46 9.86-23.45 24.33-23.45 62.7z"/><path fill="#a8c0e3" d="M376.36 298.11s0-1.08-.06-3v-3.41c0-1.32.08-2.8.15-4.43 0-.81.08-1.66.12-2.53s.19-1.78.28-2.71.2-1.88.31-2.85.31-1.95.47-3 .34-2 .53-3.06.48-2.05.73-3.1c.12-.52.25-1 .37-1.56s.31-1 .46-1.56c.32-1 .63-2.08.95-3.12.78-2 1.47-4.11 2.41-6s1.89-3.82 2.85-5.62c.54-.87 1.07-1.72 1.58-2.56s1.1-1.6 1.63-2.37 1.08-1.49 1.63-2.18 1.06-1.37 1.6-2l1.53-1.77 1.45-1.53c.89-1 1.73-1.76 2.39-2.43s1.21-1.18 1.57-1.53l.56-.54-1.94 2.25c-.61.72-1.38 1.57-2.21 2.59l-1.32 1.62-1.42 1.83c-.51.62-1 1.32-1.48 2-.26.35-.51.7-.77 1.07s-.5.75-.75 1.14c-.49.78-1.05 1.54-1.52 2.39l-1.49 2.55c-.91 1.79-1.88 3.62-2.69 5.56s-1.57 4-2.33 5.94c-.31 1-.63 2.05-1 3.07-.15.51-.32 1-.46 1.52s-.26 1-.38 1.55c-.26 1-.51 2-.76 3s-.4 2-.59 3-.4 2-.55 2.92-.27 1.89-.4 2.81-.26 1.8-.39 2.66-.16 1.7-.24 2.51c-.14 1.6-.34 3.07-.43 4.38s-.14 2.46-.2 3.41c-.1 1.98-.19 3.09-.19 3.09z"/><path fill="#5f71ae" d="M394.83 264.27c4.72-4.38 8.08-14.48 7.86-17.37a32.73 32.73 0 01-2.84 18.85 50.54 50.54 0 00-21.8 41.57c-.13-27.93 12.16-38.76 16.78-43.05z"/><path fill="#7e9acc" d="M399.37 239.6c1.57 2.36.74 12.72-2.38 17.35s-8.57 9.15-12.16 15c-2.67 4.35-4.1 1.34-2.68-3.19s3.18-11.68 7.84-18.88 8.79-11.17 9.38-10.28z" opacity=".7"/><path fill="#9eb7dd" d="M397.25 242c1.24-1 1.12 3.2.48 5.59s-8.39 11.25-9.21 11.77-.42-2.77 2.3-7.83c2.55-4.75 4.59-8.04 6.43-9.53z" opacity=".5"/><path fill="#fbf3e5" d="M420.75 82.69a3.28 3.28 0 00-1.88-.59 3.33 3.33 0 00-1.89.59c-.91.63-2 2.87-2.86 4.52-4.72 8.67-18.14 34.36-20.62 50.62l12.71 12.68h25.36l12.66-12.68c-2.47-16.26-15.89-42-20.61-50.62-.9-1.64-1.96-3.89-2.87-4.52z"/><path fill="#f2e5d1" d="M444.22 137.81c-2.48-16.27-15.88-41.93-20.6-50.6-.9-1.64-2-3.89-2.87-4.52a3.28 3.28 0 00-1.88-.59c2.61 4.19 12.7 32.37 12.7 68.41l12.63-12.65z"/><path fill="#fdfaf3" d="M417.23 85.59c.9-2.52 4.26-2.47 5.52 0a9.56 9.56 0 00-2-2.9 3.28 3.28 0 00-1.88-.59 3.33 3.33 0 00-1.89.59c-.91.63-2 2.87-2.86 4.52-4.72 8.67-18.14 34.36-20.62 50.62l12.71 12.68s.17-18.42 1.62-29.89c2.02-15.93 8.5-32.52 9.4-35.03z"/><path fill="#614d43" d="M418.89 106.63a44.15 44.15 0 0013.55-2c-3.5-7.44-6.89-13.84-8.82-17.39-.9-1.64-2-3.89-2.87-4.52a3.28 3.28 0 00-1.88-.59 3.33 3.33 0 00-1.89.59c-.91.63-2 2.87-2.86 4.52-1.93 3.55-5.32 9.94-8.82 17.37a43.75 43.75 0 0013.59 2.02z"/><path fill="#4b3c36" d="M432.44 104.6c-3.5-7.44-6.89-13.84-8.82-17.39-.9-1.64-2-3.89-2.87-4.52a3.28 3.28 0 00-1.88-.59c1.36 2.19 4.76 10.93 7.7 23.91a40.69 40.69 0 005.87-1.41z"/><path fill="#74626e" d="M422.75 85.59a9.56 9.56 0 00-2-2.9 3.28 3.28 0 00-1.88-.59 3.33 3.33 0 00-1.89.59c-.91.63-2 2.87-2.86 4.52-1.93 3.55-5.32 9.94-8.82 17.37a38.48 38.48 0 005.43 1.35 206.85 206.85 0 016.5-20.34c.9-2.52 4.26-2.47 5.52 0z"/><path fill="#53447c" d="M553.63 328.48a12.91 12.91 0 00-25.81 0v.72c.15 1.78 1.41 3.54 3.78 4.91 5 2.91 13.22 2.91 18.26 0 2.36-1.37 3.62-3.13 3.77-4.91v-.36c0-.12.01-.24 0-.36z"/><path fill="#6a507e" d="M546.33 317.21a12.89 12.89 0 00-18.51 11.27v.72c.15 1.78 1.41 3.54 3.78 4.91a17.29 17.29 0 006.48 2c-3.35-.58-5.52-4.32-4.49-8.45 1.19-4.77 6.04-11.66 12.74-10.45z"/><path fill="#4b3d6e" d="M553.63 329.2v-.36-.36a12.87 12.87 0 00-4.38-9.33c1.4 1.44 4.52 6.87 1.13 11-2.23 2.72-12.81 6.61-21.52 1.61a8.83 8.83 0 002.74 2.33c5 2.91 13.22 2.91 18.26 0 2.36-1.35 3.62-3.09 3.77-4.89z"/><path fill="#7e587b" d="M540.59 318.83c.58 1.32-.53 3.08-2.48 3.93s-4 .48-4.57-.83.53-3.08 2.48-3.93 3.98-.48 4.57.83zM533.12 324.19a1.7 1.7 0 11-2.07-.58 1.54 1.54 0 012.07.58z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#3b335f" d="M531.6 334.11c5 2.91 13.22 2.91 18.26 0a9 9 0 002.73-2.32s-4 3.88-11.84 3.88-11.89-3.89-11.89-3.89a8.83 8.83 0 002.74 2.33z"/><path fill="#5b497e" d="M533.88 338.18a17.78 17.78 0 00-35.54 0v.99c.21 2.46 1.94 4.87 5.21 6.76 6.93 4 18.2 4 25.15 0 3.25-1.89 5-4.3 5.18-6.76a4.18 4.18 0 000-.5 4 4 0 000-.49z"/><path fill="#6a507e" d="M523.83 322.66a17.77 17.77 0 00-25.49 15.52v.99c.21 2.46 1.94 4.87 5.21 6.76a23.47 23.47 0 008.91 2.78c-4.61-.79-7.59-5.94-6.17-11.63 1.64-6.59 8.31-16.08 17.54-14.42z"/><path fill="#4f4176" d="M533.88 339.17a4.18 4.18 0 000-.5 4 4 0 000-.49 17.66 17.66 0 00-6-12.85c1.93 2 6.23 9.47 1.56 15.17-3.07 3.76-17.64 9.11-29.64 2.23a12.37 12.37 0 003.78 3.2c6.93 4 18.2 4 25.15 0 3.27-1.93 4.95-4.3 5.15-6.76z"/><ellipse cx="511.08" cy="327.03" fill="#7e587b" opacity=".5" rx="5.3" ry="3.58" style="mix-blend-mode:lighten" transform="rotate(-23.71 511.074 327.023)"/><path fill="#7e587b" d="M505.64 332.27a2.34 2.34 0 11-2.85-.79 2.12 2.12 0 012.85.79z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#3b335f" d="M503.55 345.93c6.93 4 18.2 4 25.15 0a12.23 12.23 0 003.75-3.2s-5.51 5.36-16.31 5.36-16.37-5.36-16.37-5.36a12.37 12.37 0 003.78 3.2z"/><path fill="#6a4f7c" d="M502.19 344.49a22.06 22.06 0 00-44.1 0v1.23c.25 3.06 2.4 6 6.45 8.4 8.61 5 22.59 5 31.22 0 4-2.35 6.19-5.34 6.43-8.4v-.61c0-.21.02-.4 0-.62z"/><path fill="#7e587b" d="M489.71 325.24a22 22 0 00-31.62 19.25v1.23c.25 3.06 2.4 6 6.45 8.4a29.35 29.35 0 0011.07 3.45c-5.72-1-9.43-7.38-7.67-14.43 2.06-8.14 10.32-20.02 21.77-17.9z" style="mix-blend-mode:lighten"/><path fill="#5a477d" d="M502.19 345.72v-.61-.62a21.94 21.94 0 00-7.48-15.94c2.39 2.47 7.72 11.75 1.93 18.83-3.81 4.66-21.89 11.31-36.78 2.77a15.41 15.41 0 004.68 4c8.61 5 22.59 5 31.22 0 4.03-2.38 6.24-5.37 6.43-8.43z"/><path fill="#926279" d="M479.92 328c1 2.25-.91 5.26-4.24 6.72s-6.83.82-7.81-1.43.91-5.25 4.23-6.72 6.83-.81 7.82 1.43zM467.14 337.16a2.9 2.9 0 11-3.53-1 2.63 2.63 0 013.53 1z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#443b6c" d="M464.54 354.12c8.61 5 22.59 5 31.22 0a15.31 15.31 0 004.66-4c-.05.05-6.85 6.65-20.24 6.65s-20.32-6.65-20.32-6.65a15.41 15.41 0 004.68 4z"/><path fill="#4b3d6e" d="M564.55 331.5a7.8 7.8 0 00-15.59 0 1.62 1.62 0 000 .22 1.7 1.7 0 000 .22 4 4 0 002.28 3 12.2 12.2 0 0011 0 4 4 0 002.27-3 1.7 1.7 0 000-.22 1.62 1.62 0 00.04-.22z"/><path fill="#53447c" d="M560.14 324.69A7.79 7.79 0 00549 331.5a1.62 1.62 0 000 .22 1.7 1.7 0 000 .22 4 4 0 002.28 3 10.38 10.38 0 003.91 1.23c-2-.35-3.33-2.61-2.71-5.11.68-2.93 3.61-7.06 7.66-6.37z"/><path fill="#3b335f" d="M564.55 331.94a1.7 1.7 0 000-.22 1.62 1.62 0 000-.22 7.79 7.79 0 00-2.64-5.64c.84.88 2.73 4.16.68 6.66-1.35 1.65-7.74 4-13 1a5.47 5.47 0 001.66 1.4 12.2 12.2 0 0011 0 4 4 0 002.3-2.98z"/><path fill="#7e587b" d="M556.68 325.67c.35.8-.33 1.86-1.5 2.38s-2.42.29-2.77-.51.33-1.85 1.5-2.37 2.42-.29 2.77.5zM552.16 328.91a1 1 0 01-1.84.81 1 1 0 011.84-.81z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#312a53" d="M551.24 334.9a12.2 12.2 0 0011 0 5.3 5.3 0 001.65-1.4 10.62 10.62 0 01-7.16 2.35 10.75 10.75 0 01-7.19-2.35 5.47 5.47 0 001.7 1.4z"/><path fill="#53447c" d="M291.27 324.2a12.91 12.91 0 0125.81 0v.72c-.15 1.79-1.41 3.54-3.78 4.91-5 2.91-13.22 2.91-18.26 0-2.36-1.37-3.62-3.12-3.77-4.91v-.36c0-.12-.01-.24 0-.36z"/><path fill="#6a507e" d="M298.57 312.93a12.89 12.89 0 0118.51 11.27v.72c-.15 1.79-1.41 3.54-3.78 4.91a17.12 17.12 0 01-6.47 2c3.34-.58 5.51-4.32 4.48-8.44-1.19-4.77-6.03-11.7-12.74-10.46z"/><path fill="#4b3d6e" d="M291.27 324.92v-.36-.36a12.87 12.87 0 014.38-9.33c-1.4 1.44-4.52 6.88-1.13 11 2.23 2.72 12.81 6.61 21.52 1.62a9 9 0 01-2.74 2.32c-5 2.91-13.22 2.91-18.26 0-2.36-1.35-3.62-3.1-3.77-4.89z"/><path fill="#7e587b" d="M304.31 314.55c-.58 1.32.53 3.08 2.48 3.93s4 .49 4.57-.83-.53-3.08-2.48-3.93-4-.48-4.57.83zM311.78 319.91a1.7 1.7 0 102.07-.57 1.54 1.54 0 00-2.07.57z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#3b335f" d="M313.3 329.83c-5 2.91-13.22 2.91-18.26 0a9 9 0 01-2.73-2.32s4 3.89 11.84 3.89 11.85-3.89 11.85-3.89a9 9 0 01-2.7 2.32z"/><path fill="#4b3d6e" d="M291.94 297.85a7.46 7.46 0 0114.92 0v.41a3.86 3.86 0 01-2.19 2.84 11.67 11.67 0 01-10.55 0 3.85 3.85 0 01-2.18-2.84v-.41z"/><path fill="#53447c" d="M296.16 291.34a7.35 7.35 0 013.24-.75 7.47 7.47 0 017.46 7.26v.41a3.86 3.86 0 01-2.19 2.84 10.07 10.07 0 01-3.74 1.17c1.94-.34 3.19-2.5 2.59-4.88-.69-2.77-3.52-6.77-7.36-6.05z"/><path fill="#3b335f" d="M291.94 298.26v-.41a7.44 7.44 0 012.53-5.39c-.81.83-2.61 4-.65 6.36 1.29 1.58 7.4 3.82 12.44.94a5.29 5.29 0 01-1.59 1.34 11.67 11.67 0 01-10.55 0 3.85 3.85 0 01-2.18-2.84z"/><path fill="#7e587b" d="M299.48 292.27c-.34.76.3 1.78 1.43 2.27s2.31.28 2.64-.48-.31-1.78-1.43-2.27-2.31-.28-2.64.48zM303.8 295.37a.87.87 0 00.56 1.1.89.89 0 001.19-.33 1 1 0 00-1.75-.77z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#312a53" d="M304.67 301.1a11.67 11.67 0 01-10.55 0 5.36 5.36 0 01-1.58-1.34 11.62 11.62 0 0013.72 0 5.29 5.29 0 01-1.59 1.34z"/><path fill="#624b7c" d="M320.73 316.4a23.65 23.65 0 0147.29 0v1.32c-.27 3.27-2.58 6.49-6.92 9-9.23 5.33-24.22 5.33-33.47 0-4.32-2.51-6.63-5.73-6.9-9v-.66c0-.23-.02-.43 0-.66z"/><path fill="#855c75" d="M334.11 295.76A23.63 23.63 0 01368 316.4v1.32c-.27 3.27-2.58 6.49-6.92 9a31.44 31.44 0 01-11.87 3.7c6.14-1.06 10.11-7.91 8.22-15.47-2.17-8.78-11.04-21.46-23.32-19.19z"/><path fill="#5a477d" d="M320.73 317.72v-.66-.66a23.56 23.56 0 018-17.09c-2.57 2.64-8.29 12.6-2.07 20.19 4.08 5 23.47 12.11 39.42 3a16.48 16.48 0 01-5 4.26c-9.23 5.33-24.22 5.33-33.47 0-4.3-2.55-6.61-5.76-6.88-9.04z"/><path fill="#a1727c" d="M344.61 298.73c-1.05 2.41 1 5.63 4.55 7.2s7.32.88 8.37-1.53-1-5.63-4.54-7.2-7.32-.88-8.38 1.53zM358.31 308.54a3.11 3.11 0 103.79-1.05 2.81 2.81 0 00-3.79 1.05z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#4f3c68" d="M361.1 326.72c-9.23 5.33-24.22 5.33-33.47 0a16.53 16.53 0 01-5-4.26c.06.06 7.35 7.13 21.7 7.13s21.78-7.13 21.78-7.13a16.48 16.48 0 01-5.01 4.26z"/><path fill="#5b497e" d="M313.38 333.84a17.78 17.78 0 0135.54 0 4 4 0 010 .49 4.18 4.18 0 010 .5c-.2 2.46-1.93 4.87-5.2 6.76-6.93 4-18.2 4-25.15 0-3.25-1.89-5-4.3-5.19-6.76v-.5c0-.17-.01-.33 0-.49z"/><path fill="#6a507e" d="M323.44 318.32a17.76 17.76 0 0125.48 15.52 4 4 0 010 .49 4.18 4.18 0 010 .5c-.2 2.46-1.93 4.87-5.2 6.76a23.65 23.65 0 01-8.92 2.79c4.61-.8 7.6-5.95 6.18-11.63-1.64-6.6-8.31-16.13-17.54-14.43z"/><path fill="#4f4176" d="M313.38 334.83v-.5-.49a17.72 17.72 0 016-12.85c-1.93 2-6.23 9.47-1.56 15.18 3.07 3.75 17.64 9.1 29.63 2.22a12.21 12.21 0 01-3.77 3.2c-6.93 4-18.2 4-25.15 0-3.21-1.89-4.95-4.3-5.15-6.76z"/><path fill="#7e587b" d="M331.33 320.56c-.79 1.81.74 4.23 3.42 5.41s5.5.66 6.29-1.15-.73-4.24-3.41-5.41-5.5-.67-6.3 1.15zM341.63 327.93a2.34 2.34 0 102.85-.79 2.12 2.12 0 00-2.85.79z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#3b335f" d="M343.72 341.59c-6.93 4-18.2 4-25.15 0a12.52 12.52 0 01-3.76-3.19s5.52 5.35 16.31 5.35 16.37-5.36 16.37-5.36a12.21 12.21 0 01-3.77 3.2z"/><path fill="#6a4f7c" d="M347.73 334.94a22.06 22.06 0 0144.1 0v1.23c-.25 3.05-2.4 6.05-6.45 8.39-8.61 5-22.59 5-31.22 0-4-2.34-6.18-5.34-6.43-8.39v-.62c0-.21-.02-.4 0-.61z"/><path fill="#996664" d="M360.21 315.68a22 22 0 0131.62 19.26v1.23c-.25 3.05-2.4 6.05-6.45 8.39a29.35 29.35 0 01-11.07 3.44c5.72-1 9.43-7.37 7.67-14.43-2.04-8.17-10.32-20-21.77-17.89z" style="mix-blend-mode:lighten"/><path fill="#5a477d" d="M347.73 336.17v-.62-.61a21.94 21.94 0 017.48-15.94c-2.39 2.47-7.72 11.76-1.93 18.84 3.81 4.65 21.9 11.3 36.78 2.76a15.41 15.41 0 01-4.68 4c-8.61 5-22.59 5-31.22 0-4.03-2.38-6.16-5.38-6.43-8.43z"/><path fill="#cca084" d="M370 318.45c-1 2.25.91 5.26 4.24 6.72s6.83.82 7.81-1.43-.9-5.25-4.23-6.71-6.82-.83-7.82 1.42zM382.78 327.61a2.9 2.9 0 103.53-1 2.63 2.63 0 00-3.53 1z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#443b6c" d="M385.38 344.56c-8.61 5-22.59 5-31.22 0a15.31 15.31 0 01-4.66-4c.05.05 6.85 6.65 20.24 6.65s20.32-6.65 20.32-6.65a15.41 15.41 0 01-4.68 4z"/><path fill="#73537b" d="M462.08 345.79a20.14 20.14 0 00-40.26 0 5.33 5.33 0 000 .56 5.43 5.43 0 000 .57c.23 2.78 2.19 5.52 5.89 7.66 7.86 4.54 20.62 4.54 28.5 0 3.68-2.14 5.65-4.88 5.87-7.66a5.43 5.43 0 000-.57 5.33 5.33 0 000-.56z"/><path fill="#996664" d="M450.69 328.22a20.1 20.1 0 00-28.87 17.57 5.33 5.33 0 000 .56 5.43 5.43 0 000 .57c.23 2.78 2.19 5.52 5.89 7.66a26.66 26.66 0 0010.11 3.15c-5.23-.9-8.61-6.73-7-13.17 1.86-7.48 9.41-18.28 19.87-16.34z" style="mix-blend-mode:lighten"/><path fill="#624b7d" d="M462.08 346.92a5.43 5.43 0 000-.57 5.33 5.33 0 000-.56 20 20 0 00-6.83-14.55c2.19 2.25 7.05 10.73 1.76 17.19-3.47 4.25-20 10.32-33.57 2.52a13.87 13.87 0 004.27 3.63c7.86 4.54 20.62 4.54 28.5 0 3.68-2.14 5.65-4.88 5.87-7.66z"/><path fill="#cca084" d="M441.75 330.74c.9 2.06-.83 4.8-3.87 6.14s-6.23.75-7.14-1.3.84-4.8 3.87-6.14 6.23-.75 7.14 1.3zM430.08 339.1a2.65 2.65 0 11-3.22-.89 2.39 2.39 0 013.22.89z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#4f3c68" d="M427.71 354.58c7.86 4.54 20.62 4.54 28.5 0a14 14 0 004.25-3.62S454.21 357 442 357s-18.56-6-18.56-6a13.87 13.87 0 004.27 3.58z"/><path fill="#73537b" d="M378 348a19.15 19.15 0 0138.29 0 4.87 4.87 0 010 .54 4.7 4.7 0 010 .53c-.21 2.65-2.08 5.25-5.6 7.29-7.47 4.32-19.61 4.32-27.1 0-3.51-2-5.37-4.64-5.59-7.29a4.7 4.7 0 010-.53 4.87 4.87 0 010-.54z"/><path fill="#996664" d="M388.83 331.26A19.13 19.13 0 01416.28 348a4.87 4.87 0 010 .54 4.7 4.7 0 010 .53c-.21 2.65-2.08 5.25-5.6 7.29a25.57 25.57 0 01-9.61 3c5-.86 8.19-6.41 6.66-12.53-1.73-7.13-8.96-17.4-18.9-15.57z" style="mix-blend-mode:lighten"/><path fill="#624b7d" d="M378 349.05a4.7 4.7 0 010-.53 4.87 4.87 0 010-.54 19.05 19.05 0 016.5-13.84c-2.08 2.14-6.71 10.2-1.68 16.35 3.31 4 19 9.81 31.93 2.4a13.25 13.25 0 01-4.06 3.45c-7.47 4.32-19.61 4.32-27.1 0-3.52-2.04-5.38-4.64-5.59-7.29z"/><path fill="#cca084" d="M397.33 333.67c-.86 1.95.79 4.56 3.68 5.83s5.93.72 6.79-1.24-.79-4.56-3.68-5.83-5.93-.71-6.79 1.24zM408.43 341.62a2.51 2.51 0 103.06-.85 2.27 2.27 0 00-3.06.85z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#4f3c68" d="M410.68 356.34c-7.47 4.32-19.61 4.32-27.1 0a13.32 13.32 0 01-4.05-3.45c0 .05 6 5.77 17.57 5.77s17.64-5.77 17.64-5.77a13.25 13.25 0 01-4.06 3.45z"/><path fill="#73537b" d="M427.68 354.68a7.8 7.8 0 00-15.6 0 1.48 1.48 0 000 .21 1.55 1.55 0 000 .22 4 4 0 002.28 3 12.2 12.2 0 0011 0 4 4 0 002.28-3v-.43z"/><path fill="#885d7a" d="M423.26 347.87a7.79 7.79 0 00-11.18 6.81 1.48 1.48 0 000 .21 1.55 1.55 0 000 .22 4 4 0 002.28 3 10.42 10.42 0 003.92 1.22c-2-.35-3.34-2.61-2.71-5.1.72-2.93 3.64-7.11 7.69-6.36z"/><path fill="#624b7d" d="M427.68 355.11v-.43A7.79 7.79 0 00425 349c.85.87 2.73 4.16.68 6.66-1.34 1.65-7.74 4-13 1a5.58 5.58 0 001.65 1.4 12.2 12.2 0 0011 0 4 4 0 002.35-2.95z"/><path fill="#9b6779" d="M419.8 348.85c.35.79-.32 1.86-1.5 2.37s-2.41.3-2.76-.5.32-1.86 1.5-2.37 2.41-.3 2.76.5zM415.28 352.09a1 1 0 11-1.25-.35.92.92 0 011.25.35z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#4f3c68" d="M414.36 358.08a12.2 12.2 0 0011 0 5.44 5.44 0 001.65-1.4 10.59 10.59 0 01-7.16 2.35 10.7 10.7 0 01-7.18-2.35 5.58 5.58 0 001.69 1.4z"/><path fill="#4b3d6e" d="M280.35 327.22a7.8 7.8 0 0115.59 0 1.7 1.7 0 010 .22 1.62 1.62 0 010 .22 4 4 0 01-2.28 3 12.2 12.2 0 01-11 0 4 4 0 01-2.27-3 1.62 1.62 0 010-.22 1.7 1.7 0 01-.04-.22z"/><path fill="#53447c" d="M284.76 320.42a7.71 7.71 0 013.39-.78 7.79 7.79 0 017.79 7.58 1.7 1.7 0 010 .22 1.62 1.62 0 010 .22 4 4 0 01-2.28 3 10.37 10.37 0 01-3.91 1.22c2-.35 3.33-2.61 2.71-5.11-.72-2.92-3.65-7.1-7.7-6.35z"/><path fill="#3b335f" d="M280.35 327.66a1.62 1.62 0 010-.22 1.7 1.7 0 010-.22 7.74 7.74 0 012.65-5.63c-.85.87-2.74 4.15-.69 6.66 1.35 1.64 7.74 4 13 1a5.51 5.51 0 01-1.66 1.41 12.2 12.2 0 01-11 0 4 4 0 01-2.3-3z"/><path fill="#7e587b" d="M288.22 321.4c-.34.79.33 1.85 1.5 2.37s2.42.29 2.77-.5-.33-1.86-1.5-2.38-2.42-.29-2.77.51zM292.74 324.63a1 1 0 001.84.81 1 1 0 00-1.84-.81z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#312a53" d="M293.66 330.63a12.2 12.2 0 01-11 0 5.41 5.41 0 01-1.64-1.41s2.42 2.35 7.15 2.35a10.71 10.71 0 007.19-2.35 5.51 5.51 0 01-1.7 1.41z"/><path fill="#53447c" d="M305 300.28a4.51 4.51 0 019 0 .85.85 0 010 .26 2.32 2.32 0 01-1.31 1.71 7 7 0 01-6.38 0 2.31 2.31 0 01-1.32-1.71v-.26z"/><path fill="#6a507e" d="M307.57 296.35a4.62 4.62 0 012-.45 4.5 4.5 0 014.5 4.38.85.85 0 010 .26 2.32 2.32 0 01-1.31 1.71 6.11 6.11 0 01-2.27.71A2.28 2.28 0 00312 300c-.4-1.66-2.09-4.08-4.43-3.65z"/><path fill="#4b3d6e" d="M305 300.54v-.26a4.5 4.5 0 011.53-3.25c-.49.5-1.57 2.4-.39 3.85.78.95 4.47 2.3 7.51.56a3.24 3.24 0 01-.95.81 7 7 0 01-6.38 0 2.31 2.31 0 01-1.32-1.71z"/><path fill="#7e587b" d="M309.58 296.92c-.21.46.18 1.07.86 1.37s1.4.17 1.6-.29-.19-1.08-.87-1.37-1.39-.17-1.59.29zM312.19 298.79a.52.52 0 00.34.66.48.48 0 10.38-.86.53.53 0 00-.72.2z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#3b335f" d="M312.72 302.25a7 7 0 01-6.38 0 3.11 3.11 0 01-.95-.81 7 7 0 008.28 0 3.24 3.24 0 01-.95.81z"/><path fill="#53447c" d="M497.13 293a4.51 4.51 0 019 0 .62.62 0 010 .13.49.49 0 010 .12 2.32 2.32 0 01-1.31 1.72 7 7 0 01-6.38 0 2.31 2.31 0 01-1.32-1.72V293z"/><path fill="#6a507e" d="M499.68 289a4.5 4.5 0 016.46 3.93.62.62 0 010 .13.49.49 0 010 .12 2.32 2.32 0 01-1.31 1.72 6.11 6.11 0 01-2.27.71 2.28 2.28 0 001.57-2.95c-.42-1.66-2.13-4.07-4.45-3.66z"/><path fill="#4b3d6e" d="M497.13 293.2v-.2a4.49 4.49 0 011.53-3.25c-.49.5-1.58 2.4-.39 3.84.78 1 4.47 2.31 7.51.57a3.24 3.24 0 01-.95.81 7 7 0 01-6.38 0 2.31 2.31 0 01-1.32-1.77z"/><path fill="#7e587b" d="M501.68 289.59c-.2.46.19 1.07.87 1.37s1.39.17 1.6-.29-.19-1.08-.87-1.38-1.39-.16-1.6.3zM504.3 291.46a.52.52 0 00.34.66.48.48 0 10.38-.86.53.53 0 00-.72.2z" opacity=".5" style="mix-blend-mode:lighten"/><path fill="#3b335f" d="M504.83 294.92a7 7 0 01-6.38 0 3.11 3.11 0 01-.95-.81 6.08 6.08 0 004.13 1.36 6.17 6.17 0 004.15-1.36 3.24 3.24 0 01-.95.81z"/></g></svg>
    </div>

    <svg class="absolute left-0 bottom-0 w-full h-full" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 662.41 385.07" preserveAspectRatio="xMinYMax slice"><defs/><defs><radialGradient id="a" cx="368.69" cy="333.92" r="259.84" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#d37575"/><stop offset=".99" stop-color="#58448b" stop-opacity="0"/></radialGradient><radialGradient id="c" cx="2758.74" cy="334.46" r="259.84" gradientTransform="matrix(-1 0 0 1 3280.52 0)" xlink:href="#a"/><clipPath id="b"><path fill="none" d="M0 0h662.41v385.07H0z"/></clipPath></defs><g clip-path="url(#b)" style="clip-path:url(#clip-path)"><g opacity=".2"><path fill="#58448b" d="M361.11 385.53a16.81 16.81 0 00-23.11-4.32v-.59a38.54 38.54 0 00-58.5-33 26.74 26.74 0 00-45.43-12.15A16.77 16.77 0 00223 331a37.75 37.75 0 00-56.86-44.81 26.64 26.64 0 00-13.06-9.39 38.89 38.89 0 00-28.59-65.28 40.12 40.12 0 00-5.63.4 40 40 0 00-69.66-35.4A26.71 26.71 0 0015.34 169c0-.49.05-1 .05-1.45A45.51 45.51 0 00-30.13 122a45.35 45.35 0 00-20.78 5 26.93 26.93 0 002.06-10.3A26.79 26.79 0 00-75.63 90a26.37 26.37 0 00-13.09 3.43v301.82h449.83z"/><path fill="#48376d" d="M222.53 395.25h-45.64a22.82 22.82 0 1145.64 0zM323 395.25h-66.4a15.71 15.71 0 1128.31-9.73 22.8 22.8 0 0138.09 9.73zM134.15 360.36a27.23 27.23 0 00-12.43 3 18.08 18.08 0 00-31.4-17.06A18.75 18.75 0 0061 331.06a30.41 30.41 0 00.5-5.35A29 29 0 007.49 311a5.85 5.85 0 000-.6A18.77 18.77 0 00-10 291.66 22.83 22.83 0 005.65 270a22.83 22.83 0 00-22.83-22.82 22.72 22.72 0 00-10 2.34 31.25 31.25 0 002.27-11.63 31.25 31.25 0 00-31.25-31.25 31.15 31.15 0 00-16.66 4.84 18.09 18.09 0 00-11.24-6.71 22.75 22.75 0 006.86-16.29 22.78 22.78 0 00-11.5-19.8v226.57h249a26.5 26.5 0 001.1-7.65 27.24 27.24 0 00-27.25-27.24z"/><path fill="#3e3063" d="M80.62 395.25H23.39a29.79 29.79 0 0157.23 0zM7.43 381.31a39.28 39.28 0 01-2.54 13.94h-93.61V271.32a43 43 0 0134 42.07 42.63 42.63 0 01-2.59 14.74h.08a16.78 16.78 0 0116.63 14.69 39.72 39.72 0 018.58-.94 39.44 39.44 0 0139.45 39.43z"/><circle cx="101.05" cy="240.18" r="12.28" fill="#48376d" transform="rotate(-45 101.048 240.185)"/><circle cx="86.62" cy="303.13" r="8.6" fill="#48376d"/><path fill="#48376d" d="M136.23 339a5.75 5.75 0 115.75 5.75 5.75 5.75 0 01-5.75-5.75zM239 373.74a5.74 5.74 0 115.74 5.75 5.74 5.74 0 01-5.74-5.75zM6.61 287.71a5.75 5.75 0 115.74 5.75 5.74 5.74 0 01-5.74-5.75zM124.5 248.67a5.87 5.87 0 115.87 5.87 5.87 5.87 0 01-5.87-5.87z"/><path fill="#58448b" d="M241.25 311a5.55 5.55 0 115.55 5.55 5.55 5.55 0 01-5.55-5.55z"/><circle cx="181.19" cy="251.6" r="9.63" fill="#58448b" transform="rotate(-25.44 181.23 251.633)"/><path fill="#3e3063" d="M19.23 365.39a4.85 4.85 0 114.85 4.85 4.85 4.85 0 01-4.85-4.85z"/><circle cx="95.21" cy="370.24" r="9.53" fill="#3e3063" transform="rotate(-76.66 95.223 370.242)"/><path fill="#ad6475" d="M272.13 353.47a38.5 38.5 0 017.41-5.85 26.68 26.68 0 00-33.08-19.53 26.74 26.74 0 0125.67 25.38zM217.33 316.32a37.6 37.6 0 01-4.54 18 16.72 16.72 0 019.94-3.27h.27a37.75 37.75 0 00-35-51.75h-.81a37.76 37.76 0 0130.14 37.02zM206.78 342.49a37.63 37.63 0 01-26.39 11.56 37.85 37.85 0 0025.67-3.86 16 16 0 01-.18-2.31 16.61 16.61 0 01.9-5.39z"/><path fill="#ad6475" d="M223 331h-.29a16.72 16.72 0 00-9.94 3.27 37.9 37.9 0 01-6 8.19 16.61 16.61 0 00-.9 5.39 16 16 0 00.18 2.31A37.88 37.88 0 00223 331zM138.3 276.3a26.39 26.39 0 016.45-.82 26.8 26.8 0 018.35 1.34 38.89 38.89 0 00-9.24-60.11 38.91 38.91 0 01-5.56 59.59zM105.79 205.87v.88a38.75 38.75 0 0110.56-1.46c1.23 0 2.45.06 3.65.17.11-1.16.17-2.34.17-3.53A40 40 0 0062.52 166c1.08-.09 2.16-.14 3.26-.14a40 40 0 0140.01 40.01z"/><path fill="#ad6475" d="M105.77 206.75a40 40 0 01-1.65 10.56 38.73 38.73 0 0114.76-5.31 39.62 39.62 0 001.1-6.49c-1.2-.11-2.42-.17-3.65-.17a38.75 38.75 0 00-10.56 1.41z"/><path fill="url(#a)" d="M361.11 385.53a16.81 16.81 0 00-23.11-4.32v-.59a38.54 38.54 0 00-58.5-33 26.74 26.74 0 00-45.43-12.15A16.77 16.77 0 00223 331a37.75 37.75 0 00-56.86-44.81 26.64 26.64 0 00-13.06-9.39 38.89 38.89 0 00-28.59-65.28 40.12 40.12 0 00-5.63.4 40 40 0 00-69.66-35.4A26.71 26.71 0 0015.34 169c0-.49.05-1 .05-1.45A45.51 45.51 0 00-30.13 122a45.35 45.35 0 00-20.78 5 26.93 26.93 0 002.06-10.3A26.79 26.79 0 00-75.63 90a26.37 26.37 0 00-13.09 3.43v301.82h449.83z" style="mix-blend-mode:lighten"/></g><g opacity=".2"><path fill="#58448b" d="M529.35 386.08a16.8 16.8 0 0123.07-4.33v-.59a38.55 38.55 0 0158.51-33A26.74 26.74 0 01656.34 336a16.77 16.77 0 0111.1-4.45 37.76 37.76 0 0156.86-44.81 26.7 26.7 0 0113.06-9.39 38.9 38.9 0 0134.22-64.87 40 40 0 0169.66-35.41 26.71 26.71 0 0133.88-7.58v-1.45a45.52 45.52 0 0166.3-40.48 26.78 26.78 0 0124.67-37.06 26.37 26.37 0 0113.09 3.43v301.86H529.35z"/><path fill="#48376d" d="M567.43 395.79h66.4a15.7 15.7 0 10-28.31-9.73 22.8 22.8 0 00-38.09 9.73zM651.46 374.29a5.74 5.74 0 10-5.74 5.74 5.74 5.74 0 005.74-5.74z"/><circle cx="643.66" cy="311.51" r="5.55" fill="#58448b"/><path fill="#ad6475" d="M618.33 354a38.58 38.58 0 00-7.41-5.85 26.76 26.76 0 0126-20.5 27.05 27.05 0 017.07 1A26.75 26.75 0 00618.33 354z"/><path fill="url(#c)" d="M529.35 386.08a16.8 16.8 0 0123.07-4.33v-.59a38.55 38.55 0 0158.51-33A26.74 26.74 0 01656.34 336a16.77 16.77 0 0111.1-4.45 37.76 37.76 0 0156.86-44.81 26.7 26.7 0 0113.06-9.39 38.9 38.9 0 0134.22-64.87 40 40 0 0169.66-35.41 26.71 26.71 0 0133.88-7.58v-1.45a45.52 45.52 0 0166.3-40.48 26.78 26.78 0 0124.67-37.06 26.37 26.37 0 0113.09 3.43v301.86H529.35z" style="mix-blend-mode:lighten"/></g></g></svg>
</div>''', '''<!-- component -->
<div class="py-6">
  <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl">
        <div class="hidden lg:block lg:w-1/2 bg-cover" style="background-image:url('https://images.unsplash.com/photo-1546514714-df0ccc50d7bf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80')"></div>
        <div class="w-full p-8 lg:w-1/2">
            <h2 class="text-2xl font-semibold text-gray-700 text-center">Brand</h2>
            <p class="text-xl text-gray-600 text-center">Welcome back!</p>
            <a href="#" class="flex items-center justify-center mt-4 text-white rounded-lg shadow-md hover:bg-gray-100">
                <div class="px-4 py-3">
                    <svg class="h-6 w-6" viewBox="0 0 40 40">
                        <path d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.045 27.2142 24.3525 30 20 30C14.4775 30 10 25.5225 10 20C10 14.4775 14.4775 9.99999 20 9.99999C22.5492 9.99999 24.8683 10.9617 26.6342 12.5325L31.3483 7.81833C28.3717 5.04416 24.39 3.33333 20 3.33333C10.7958 3.33333 3.33335 10.7958 3.33335 20C3.33335 29.2042 10.7958 36.6667 20 36.6667C29.2042 36.6667 36.6667 29.2042 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z" fill="#FFC107"/>
                        <path d="M5.25497 12.2425L10.7308 16.2583C12.2125 12.59 15.8008 9.99999 20 9.99999C22.5491 9.99999 24.8683 10.9617 26.6341 12.5325L31.3483 7.81833C28.3716 5.04416 24.39 3.33333 20 3.33333C13.5983 3.33333 8.04663 6.94749 5.25497 12.2425Z" fill="#FF3D00"/>
                        <path d="M20 36.6667C24.305 36.6667 28.2167 35.0192 31.1742 32.34L26.0159 27.975C24.3425 29.2425 22.2625 30 20 30C15.665 30 11.9842 27.2359 10.5975 23.3784L5.16254 27.5659C7.92087 32.9634 13.5225 36.6667 20 36.6667Z" fill="#4CAF50"/>
                        <path d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.7592 25.1975 27.56 26.805 26.0133 27.9758C26.0142 27.975 26.015 27.975 26.0158 27.9742L31.1742 32.3392C30.8092 32.6708 36.6667 28.3333 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z" fill="#1976D2"/>
                    </svg>
                </div>
                <h1 class="px-4 py-3 w-5/6 text-center text-gray-600 font-bold">Sign in with Google</h1>
            </a>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 lg:w-1/4"></span>
                <a href="#" class="text-xs text-center text-gray-500 uppercase">or login with email</a>
                <span class="border-b w-1/5 lg:w-1/4"></span>
            </div>
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">Email Address</label>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="email">
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Password</label>
                    <a href="#" class="text-xs text-gray-500">Forget Password?</a>
                </div>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password">
            </div>
            <div class="mt-8">
                <button class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Login</button>
            </div>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <a href="#" class="text-xs text-gray-500 uppercase">or sign up</a>
                <span class="border-b w-1/5 md:w-1/4"></span>
            </div>
        </div>
    </div>
</div>''',]
About = ['''<div class="overflow-hidden bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4">
        <div class="lg:max-w-lg">
          <h2 class="text-base font-semibold leading-7 text-indigo-600">Deploy faster</h2>
          <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">A better workflow</p>
          <p class="mt-6 text-lg leading-8 text-gray-600">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.</p>
          <dl class="mt-10 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                  <path fill-rule="evenodd" d="M5.5 17a4.5 4.5 0 01-1.44-8.765 4.5 4.5 0 018.302-3.046 3.5 3.5 0 014.504 4.272A4 4 0 0115 17H5.5zm3.75-2.75a.75.75 0 001.5 0V9.66l1.95 2.1a.75.75 0 101.1-1.02l-3.25-3.5a.75.75 0 00-1.1 0l-3.25 3.5a.75.75 0 101.1 1.02l1.95-2.1v4.59z" clip-rule="evenodd" />
                </svg>
                Push to deploy.
              </dt>
              <dd class="inline">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.</dd>
            </div>

            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                  <path fill-rule="evenodd" d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z" clip-rule="evenodd" />
                </svg>
                SSL certificates.
              </dt>
              <dd class="inline">Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo.</dd>
            </div>

            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                  <path d="M4.632 3.533A2 2 0 016.577 2h6.846a2 2 0 011.945 1.533l1.976 8.234A3.489 3.489 0 0016 11.5H4c-.476 0-.93.095-1.344.267l1.976-8.234z" />
                  <path fill-rule="evenodd" d="M4 13a2 2 0 100 4h12a2 2 0 100-4H4zm11.24 2a.75.75 0 01.75-.75H16a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75h-.01a.75.75 0 01-.75-.75V15zm-2.25-.75a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75H13a.75.75 0 00.75-.75V15a.75.75 0 00-.75-.75h-.01z" clip-rule="evenodd" />
                </svg>
                Database backups.
              </dt>
              <dd class="inline">Ac tincidunt sapien vehicula erat auctor pellentesque rhoncus. Et magna sit morbi lobortis.</dd>
            </div>
          </dl>
        </div>
      </div>
      <img src="https://tailwindui.com/img/component-images/dark-project-app-screenshot.png" alt="Product screenshot" class="w-[48rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem] md:-ml-4 lg:-ml-0" width="2432" height="1442">
    </div>
  </div>
</div>
''', '''<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:text-center">
      <h2 class="text-base font-semibold leading-7 text-indigo-600">Deploy faster</h2>
      <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Everything you need to deploy your app</p>
      <p class="mt-6 text-lg leading-8 text-gray-600">Quis tellus eget adipiscing convallis sit sit eget aliquet quis. Suspendisse eget egestas a elementum pulvinar et feugiat blandit at. In mi viverra elit nunc.</p>
    </div>
    <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
      <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
        <div class="relative pl-16">
          <dt class="text-base font-semibold leading-7 text-gray-900">
            <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
              <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 16.5V9.75m0 0l3 3m-3-3l-3 3M6.75 19.5a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z" />
              </svg>
            </div>
            Push to deploy
          </dt>
          <dd class="mt-2 text-base leading-7 text-gray-600">Morbi viverra dui mi arcu sed. Tellus semper adipiscing suspendisse semper morbi. Odio urna massa nunc massa.</dd>
        </div>

        <div class="relative pl-16">
          <dt class="text-base font-semibold leading-7 text-gray-900">
            <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
              <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
              </svg>
            </div>
            SSL certificates
          </dt>
          <dd class="mt-2 text-base leading-7 text-gray-600">Sit quis amet rutrum tellus ullamcorper ultricies libero dolor eget. Sem sodales gravida quam turpis enim lacus amet.</dd>
        </div>

        <div class="relative pl-16">
          <dt class="text-base font-semibold leading-7 text-gray-900">
            <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
              <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
              </svg>
            </div>
            Simple queues
          </dt>
          <dd class="mt-2 text-base leading-7 text-gray-600">Quisque est vel vulputate cursus. Risus proin diam nunc commodo. Lobortis auctor congue commodo diam neque.</dd>
        </div>

        <div class="relative pl-16">
          <dt class="text-base font-semibold leading-7 text-gray-900">
            <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
              <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M7.864 4.243A7.5 7.5 0 0119.5 10.5c0 2.92-.556 5.709-1.568 8.268M5.742 6.364A7.465 7.465 0 004.5 10.5a7.464 7.464 0 01-1.15 3.993m1.989 3.559A11.209 11.209 0 008.25 10.5a3.75 3.75 0 117.5 0c0 .527-.021 1.049-.064 1.565M12 10.5a14.94 14.94 0 01-3.6 9.75m6.633-4.596a18.666 18.666 0 01-2.485 5.33" />
              </svg>
            </div>
            Advanced security
          </dt>
          <dd class="mt-2 text-base leading-7 text-gray-600">Arcu egestas dolor vel iaculis in ipsum mauris. Tincidunt mattis aliquet hac quis. Id hac maecenas ac donec pharetra eget.</dd>
        </div>
      </dl>
    </div>
  </div>
</div>
''', '''<!-- component -->
<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/zxcvbn/4.4.2/zxcvbn.js"></script>

<style>@import url('https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.3.45/css/materialdesignicons.min.css')</style>

<div class="min-w-screen min-h-screen bg-gray-900 flex items-center justify-center px-5 py-5">
    <div class="bg-gray-100 text-gray-500 rounded-3xl shadow-xl w-full overflow-hidden" style="max-width:1000px">
        <div class="md:flex w-full">
            <div class="hidden md:block w-1/2 bg-indigo-500 py-10 px-10">
                <svg id="a87032b8-5b37-4b7e-a4d9-4dbfbe394641" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 744.84799 747.07702"><path id="fa3b9e12-7275-481e-bee9-64fd9595a50d" data-name="Path 1" d="M299.205,705.80851l-6.56-25.872a335.96693,335.96693,0,0,0-35.643-12.788l-.828,12.024-3.358-13.247c-15.021-4.29394-25.24-6.183-25.24-6.183s13.8,52.489,42.754,92.617l33.734,5.926-26.207,3.779a135.92592,135.92592,0,0,0,11.719,12.422c42.115,39.092,89.024,57.028,104.773,40.06s-5.625-62.412-47.74-101.5c-13.056-12.119-29.457-21.844-45.875-29.5Z" transform="translate(-227.576 -76.46149)" fill="#f2f2f2"/><path id="bde08021-c30f-4979-a9d8-cb90b72b5ca2" data-name="Path 2" d="M361.591,677.70647l7.758-25.538a335.93951,335.93951,0,0,0-23.9-29.371l-6.924,9.865,3.972-13.076c-10.641-11.436-18.412-18.335-18.412-18.335s-15.315,52.067-11.275,101.384l25.815,22.51-24.392-10.312a135.91879,135.91879,0,0,0,3.614,16.694c15.846,55.234,46.731,94.835,68.983,88.451s27.446-56.335,11.6-111.569c-4.912-17.123-13.926-33.926-24.023-48.965Z" transform="translate(-227.576 -76.46149)" fill="#f2f2f2"/><path id="b3ac2088-de9b-4f7f-bc99-0ed9705c1a9d" data-name="Path 22" d="M747.327,253.4445h-4.092v-112.1a64.883,64.883,0,0,0-64.883-64.883H440.845a64.883,64.883,0,0,0-64.883,64.883v615a64.883,64.883,0,0,0,64.883,64.883H678.352a64.883,64.883,0,0,0,64.882-64.883v-423.105h4.092Z" transform="translate(-227.576 -76.46149)" fill="#e6e6e6"/><path id="b2715b96-3117-487c-acc0-20904544b5b7" data-name="Path 23" d="M680.97,93.3355h-31a23.02,23.02,0,0,1-21.316,31.714H492.589a23.02,23.02,0,0,1-21.314-31.714H442.319a48.454,48.454,0,0,0-48.454,48.454v614.107a48.454,48.454,0,0,0,48.454,48.454H680.97a48.454,48.454,0,0,0,48.454-48.454h0V141.7885a48.454,48.454,0,0,0-48.454-48.453Z" transform="translate(-227.576 -76.46149)" fill="#fff"/><path id="b06d66ec-6c84-45dd-8c27-1263a6253192" data-name="Path 6" d="M531.234,337.96451a24.437,24.437,0,0,1,12.23-21.174,24.45,24.45,0,1,0,0,42.345A24.43391,24.43391,0,0,1,531.234,337.96451Z" transform="translate(-227.576 -76.46149)" fill="#ccc"/><path id="e73810fe-4cf4-40cc-8c7c-ca544ce30bd4" data-name="Path 7" d="M561.971,337.96451a24.43594,24.43594,0,0,1,12.23-21.174,24.45,24.45,0,1,0,0,42.345A24.43391,24.43391,0,0,1,561.971,337.96451Z" transform="translate(-227.576 -76.46149)" fill="#ccc"/><circle id="a4813fcf-056e-4514-bb8b-e6506f49341f" data-name="Ellipse 1" cx="364.43401" cy="261.50202" r="24.45" fill="#6c63ff"/><path id="bbe451c3-febc-41ba-8083-4c8307a2e73e" data-name="Path 8" d="M632.872,414.3305h-142.5a5.123,5.123,0,0,1-5.117-5.117v-142.5a5.123,5.123,0,0,1,5.117-5.117h142.5a5.123,5.123,0,0,1,5.117,5.117v142.5A5.123,5.123,0,0,1,632.872,414.3305Zm-142.5-150.686a3.073,3.073,0,0,0-3.07,3.07v142.5a3.073,3.073,0,0,0,3.07,3.07h142.5a3.073,3.073,0,0,0,3.07-3.07v-142.5a3.073,3.073,0,0,0-3.07-3.07Z" transform="translate(-227.576 -76.46149)" fill="#ccc"/><rect id="bb28937d-932f-4fdf-befe-f406e51091fe" data-name="Rectangle 1" x="218.56201" y="447.10197" width="218.552" height="2.047" fill="#ccc"/><circle id="fcef55fc-4968-45b2-93bb-1a1080c85fc7" data-name="Ellipse 2" cx="225.46401" cy="427.41999" r="6.902" fill="#6c63ff"/><rect id="ff33d889-4c74-4b91-85ef-b4882cc8fe76" data-name="Rectangle 2" x="218.56201" y="516.11803" width="218.552" height="2.047" fill="#ccc"/><circle id="e8fa0310-b872-4adf-aedd-0c6eda09f3b8" data-name="Ellipse 3" cx="225.46401" cy="496.43702" r="6.902" fill="#6c63ff"/><path d="M660.69043,671.17188H591.62207a4.50493,4.50493,0,0,1-4.5-4.5v-24.208a4.50492,4.50492,0,0,1,4.5-4.5h69.06836a4.50491,4.50491,0,0,1,4.5,4.5v24.208A4.50492,4.50492,0,0,1,660.69043,671.17188Z" transform="translate(-227.576 -76.46149)" fill="#6c63ff"/><circle id="e12ee00d-aa4a-4413-a013-11d20b7f97f7" data-name="Ellipse 7" cx="247.97799" cy="427.41999" r="6.902" fill="#6c63ff"/><circle id="f58f497e-6949-45c8-be5f-eee2aa0f6586" data-name="Ellipse 8" cx="270.492" cy="427.41999" r="6.902" fill="#6c63ff"/><circle id="b4d4939a-c6e6-4f4d-ba6c-e8b05485017d" data-name="Ellipse 9" cx="247.97799" cy="496.43702" r="6.902" fill="#6c63ff"/><circle id="aff120b1-519b-4e96-ac87-836aa55663de" data-name="Ellipse 10" cx="270.492" cy="496.43702" r="6.902" fill="#6c63ff"/><path id="f1094013-1297-477a-ac57-08eac07c4bd5" data-name="Path 88" d="M969.642,823.53851H251.656c-1.537,0-2.782-.546-2.782-1.218s1.245-1.219,2.782-1.219H969.642c1.536,0,2.782.546,2.782,1.219S971.178,823.53851,969.642,823.53851Z" transform="translate(-227.576 -76.46149)" fill="#3f3d56"/><path d="M792.25256,565.92292a10.09371,10.09371,0,0,1,1.41075.78731l44.8523-19.14319,1.60093-11.81526,17.92157-.10956-1.05873,27.0982-59.19987,15.65584a10.60791,10.60791,0,0,1-.44749,1.20835,10.2346,10.2346,0,1,1-5.07946-13.68169Z" transform="translate(-227.576 -76.46149)" fill="#ffb8b8"/><polygon points="636.98 735.021 624.72 735.021 618.888 687.733 636.982 687.734 636.98 735.021" fill="#ffb8b8"/><path d="M615.96281,731.51778h23.64387a0,0,0,0,1,0,0v14.88687a0,0,0,0,1,0,0H601.076a0,0,0,0,1,0,0v0A14.88686,14.88686,0,0,1,615.96281,731.51778Z" fill="#2f2e41"/><polygon points="684.66 731.557 672.459 732.759 662.018 686.271 680.025 684.497 684.66 731.557" fill="#ffb8b8"/><path d="M891.68576,806.12757h23.64387a0,0,0,0,1,0,0v14.88687a0,0,0,0,1,0,0H876.7989a0,0,0,0,1,0,0v0A14.88686,14.88686,0,0,1,891.68576,806.12757Z" transform="translate(-303.00873 15.2906) rotate(-5.62529)" fill="#2f2e41"/><circle cx="640.3925" cy="384.57375" r="24.56103" fill="#ffb8b8"/><path d="M849.55636,801.91945a4.47086,4.47086,0,0,1-4.415-3.69726c-6.34571-35.22559-27.08789-150.40528-27.584-153.59571a1.42684,1.42684,0,0,1-.01562-.22168v-8.58789a1.489,1.489,0,0,1,.27929-.87207l2.74024-3.83789a1.47845,1.47845,0,0,1,1.14355-.625c15.62207-.73242,66.78418-2.8789,69.25586.209h0c2.48242,3.10351,1.60547,12.50683,1.4043,14.36035l.00977.19336,22.98535,146.99512a4.51238,4.51238,0,0,1-3.71485,5.13476l-14.35644,2.36524a4.52127,4.52127,0,0,1-5.02539-3.09278c-4.44043-14.18847-19.3291-61.918-24.48926-80.38672a.49922.49922,0,0,0-.98047.13868c.25781,17.60546.88086,62.52343,1.0957,78.0371l.02344,1.6709a4.51811,4.51811,0,0,1-4.09277,4.53614l-13.84375,1.25781C849.83565,801.91359,849.695,801.91945,849.55636,801.91945Z" transform="translate(-227.576 -76.46149)" fill="#2f2e41"/><path id="ae7af94f-88d7-4204-9f07-e3651de85c05" data-name="Path 99" d="M852.38089,495.2538c-4.28634,2.548-6.85116,7.23043-8.32276,11.9951a113.681,113.681,0,0,0-4.88444,27.15943l-1.55553,27.60021-19.25508,73.1699c16.68871,14.1207,26.31542,10.91153,48.78049-.63879s25.03222,3.85117,25.03222,3.85117l4.49236-62.25839,6.41837-68.03232a30.16418,30.16418,0,0,0-4.86143-4.67415,49.65848,49.65848,0,0,0-42.44229-8.99538Z" transform="translate(-227.576 -76.46149)" fill="#ffffff"/><path d="M846.12661,580.70047a10.52561,10.52561,0,0,1,1.50061.70389l44.34832-22.1972.736-12.02551,18.2938-1.26127.98041,27.4126L852.7199,592.93235a10.4958,10.4958,0,1,1-6.59329-12.23188Z" transform="translate(-227.576 -76.46149)" fill="#ffb8b8"/><path id="a6768b0e-63d0-4b31-8462-9b2e0b00f0fd" data-name="Path 101" d="M902.76552,508.41151c10.91151,3.85117,12.83354,45.57369,12.83354,45.57369-12.8367-7.06036-28.24139,4.49318-28.24139,4.49318s-3.20916-10.91154-7.06034-25.03223a24.52987,24.52987,0,0,1,5.13436-23.10625S891.854,504.558,902.76552,508.41151Z" transform="translate(-227.576 -76.46149)" fill="#ffffff"/><path id="bfd7963f-0cf8-4885-9d3a-2c00bccda2e3" data-name="Path 102" d="M889.99122,467.53052c-3.06-2.44837-7.23517,2.00173-7.23517,2.00173l-2.4484-22.03349s-15.30095,1.8329-25.0935-.61161-11.32255,8.87513-11.32255,8.87513a78.57978,78.57978,0,0,1-.30582-13.77092c.61158-5.50838,8.56838-11.01675,22.6451-14.68932S887.6518,439.543,887.6518,439.543C897.44542,444.43877,893.05121,469.97891,889.99122,467.53052Z" transform="translate(-227.576 -76.46149)" fill="#2f2e41"/></svg>
            </div>
            <div class="w-full md:w-1/2 py-10 px-5 md:px-10">
                <div class="text-center mb-10">
                    <h1 class="font-bold text-3xl text-gray-900">REGISTER</h1>
                    <p>Enter your information to register</p>
                </div>
                <div>
                    <div class="flex -mx-3">
                        <div class="w-1/2 px-3 mb-5">
                            <label for="" class="text-xs font-semibold px-1">First name</label>
                            <div class="flex">
                                <div class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"><i class="mdi mdi-account-outline text-gray-400 text-lg"></i></div>
                                <input type="text" class="w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500" placeholder="John">
                            </div>
                        </div>
                        <div class="w-1/2 px-3 mb-5">
                            <label for="" class="text-xs font-semibold px-1">Last name</label>
                            <div class="flex">
                                <div class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"><i class="mdi mdi-account-outline text-gray-400 text-lg"></i></div>
                                <input type="text" class="w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500" placeholder="Smith">
                            </div>
                        </div>
                    </div>
                    <div class="flex -mx-3">
                        <div class="w-full px-3 mb-5">
                            <label for="" class="text-xs font-semibold px-1">Email</label>
                            <div class="flex">
                                <div class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"><i class="mdi mdi-email-outline text-gray-400 text-lg"></i></div>
                                <input type="email" class="w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500" placeholder="johnsmith@example.com">
                            </div>
                        </div>
                    </div>
                    <div class="flex -mx-3">
                        <div class="w-full px-3 mb-12">
                            <label for="" class="text-xs font-semibold px-1">Password</label>
                            <div class="flex">
                                <div class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"><i class="mdi mdi-lock-outline text-gray-400 text-lg"></i></div>
                                <input type="password" class="w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500" placeholder="************">
                            </div>
                        </div>
                    </div>
                    <div class="flex -mx-3">
                        <div class="w-full px-3 mb-5">
                            <button class="block w-full max-w-xs mx-auto bg-indigo-500 hover:bg-indigo-700 focus:bg-indigo-700 text-white rounded-lg px-3 py-3 font-semibold">REGISTER NOW</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- BUY ME A BEER AND HELP SUPPORT OPEN-SOURCE RESOURCES -->
<div class="flex items-end justify-end fixed bottom-0 right-0 mb-4 mr-4 z-10">
    <div>
        <a title="Buy me a beer" href="https://www.buymeacoffee.com/scottwindon" target="_blank" class="block w-16 h-16 rounded-full transition-all shadow hover:shadow-lg transform hover:scale-110 hover:rotate-12">
            <img class="object-cover object-center w-full h-full rounded-full" src="https://i.pinimg.com/originals/60/fd/e8/60fde811b6be57094e0abc69d9c2622a.jpg"/>
        </a>
    </div>
</div>''', '''<!-- component -->
<div class="h-screen flex items-center justify-center">

  <card class="relative h-[30rem] sm:h-96 w-[35rem] rounded-lg">

    <!-- Background Image -->
    <img src="https://picsum.photos/seed/1840/1000/600" class="object-cover w-full h-full rounded-lg" />
    
    <!-- Content -->
    <div class="absolute w-full h-full bottom-0 bg-gradient-to-r from-fuchsia-700/30 to-violet-700 rounded-lg flex flex-col items-center justify-center text-center">
    
        <!-- Company Logo -->
        <img src="https://github.githubassets.com/images/modules/site/enterprise/launchpad/logos/logo-dowjones.svg" />

        <!-- Quotes -->
        <p class="text-lg px-14 text-gray-300 mt-10">
          GitHub helps us ensure that we have our security controls baked into our pipelines all the way from the first line of code we’re writing.
        </p>

        <!-- Photo -->
        <img src="https://picsum.photos/50/50" class="rounded-full border-2 mt-8" />

        <!-- Title -->
        <p class="text-base font-bold px-14 text-gray-300 mt-3">
          Chief Information Security Officer
        </p>

        <p class="text-sm font-light px-14 text-gray-300 ">
          Dow Jones
        </p>

    </div>

  </card>

</div>''', '''<!-- component -->
<div>
    <div class="relative min-h-screen  grid bg-black ">
      <div class="flex flex-col sm:flex-row items-center md:items-start sm:justify-center md:justify-start flex-auto min-w-0 ">
        <div  class="relative sm:w-1/2 xl:w-3/5 bg-blue-500 h-full hidden md:flex flex-auto items-center justify-center p-10 overflow-hidden  text-white bg-no-repeat bg-cover relative" style="background-image: url(https://i.postimg.cc/mrgPMqpP/logo.png);">
          <div class="absolute bg-black  opacity-25 inset-0 z-0"></div>
          <div class="w-full  lg:max-w-2xl md:max-w-md z-10 items-center text-center ">
            <div class=" font-bold leading-tight mb-6 mx-auto w-full content-center items-center ">
          
            </div>
          </div>
        </div>

        <div class="md:flex md:items-center md:justify-left w-full sm:w-auto md:h-full xl:w-1/2 p-8  md:p-10 lg:p-14 sm:rounded-lg md:rounded-none ">
            <div class="max-w-xl w-full space-y-12">
              <div class="lg:text-left text-center">
          
                <div class="flex items-center justify-center ">
                  <div class="bg-black flex flex-col w-80 border border-gray-900 rounded-lg px-8 py-10">
                  
                  <form [formGroup]="createaccount" class="flex flex-col space-y-8 mt-10">
                 <label class="font-bold text-lg text-white " >Account Number</label> 
                 <input type="text" formControlName="accnum" placeholder="Account number" class="border rounded-lg py-3 px-3 mt-4 bg-black border-indigo-600 placeholder-white-500 text-white">
                  <label class="font-bold text-lg text-white">Pin</label> 
                  <input type="password" formControlName="pin" placeholder="****" class="border rounded-lg py-3 px-3 bg-black border-indigo-600 placeholder-white-500 text-white">
                  <label class="font-bold text-lg text-white " >Initial Deposit</label> 
                  <input type="text" formControlName="amount" placeholder="Amount in INR" class="border rounded-lg py-3 px-3 mt-4 bg-black border-indigo-600 placeholder-white-500 text-white">
                    <button (click)="onSubmit()" class="border border-indigo-600 bg-black text-white rounded-lg py-3 font-semibold" routerLink="/dashboard">Create Account</button>
                  </form>
                </div>
                </div>
              
            </div>
              
            </div>''', '''<!-- component -->
<div class="h-screen bg-white flex flex-col space-y-10 justify-center items-center">
 
  <!-- linkedin logo -->
 <div class=" flex w-96 ">
    <svg class="w-32  " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 84 21" preserveAspectRatio="xMinYMin meet" version="1.1" focusable="false" class="lazy-loaded">
      <g class="inbug" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <path d="M19.479,0 L1.583,0 C0.727,0 0,0.677 0,1.511 L0,19.488 C0,20.323 0.477,21 1.333,21 L19.229,21 C20.086,21 21,20.323 21,19.488 L21,1.511 C21,0.677 20.336,0 19.479,0" class="bug-text-color" transform="translate(63.000000, 0.000000)"></path>
        <path d="M82.479,0 L64.583,0 C63.727,0 63,0.677 63,1.511 L63,19.488 C63,20.323 63.477,21 64.333,21 L82.229,21 C83.086,21 84,20.323 84,19.488 L84,1.511 C84,0.677 83.336,0 82.479,0 Z M71,8 L73.827,8 L73.827,9.441 L73.858,9.441 C74.289,8.664 75.562,7.875 77.136,7.875 C80.157,7.875 81,9.479 81,12.45 L81,18 L78,18 L78,12.997 C78,11.667 77.469,10.5 76.227,10.5 C74.719,10.5 74,11.521 74,13.197 L74,18 L71,18 L71,8 Z M66,18 L69,18 L69,8 L66,8 L66,18 Z M69.375,4.5 C69.375,5.536 68.536,6.375 67.5,6.375 C66.464,6.375 65.625,5.536 65.625,4.5 C65.625,3.464 66.464,2.625 67.5,2.625 C68.536,2.625 69.375,3.464 69.375,4.5 Z" class="background" fill="#0a66c2"></path>
      </g>
      <g class="linkedin-text">
        <path d="M60,18 L57.2,18 L57.2,16.809 L57.17,16.809 C56.547,17.531 55.465,18.125 53.631,18.125 C51.131,18.125 48.978,16.244 48.978,13.011 C48.978,9.931 51.1,7.875 53.725,7.875 C55.35,7.875 56.359,8.453 56.97,9.191 L57,9.191 L57,3 L60,3 L60,18 Z M54.479,10.125 C52.764,10.125 51.8,11.348 51.8,12.974 C51.8,14.601 52.764,15.875 54.479,15.875 C56.196,15.875 57.2,14.634 57.2,12.974 C57.2,11.268 56.196,10.125 54.479,10.125 L54.479,10.125 Z" fill="#0a66c2"></path>
        <path d="M47.6611,16.3889 C46.9531,17.3059 45.4951,18.1249 43.1411,18.1249 C40.0001,18.1249 38.0001,16.0459 38.0001,12.7779 C38.0001,9.8749 39.8121,7.8749 43.2291,7.8749 C46.1801,7.8749 48.0001,9.8129 48.0001,13.2219 C48.0001,13.5629 47.9451,13.8999 47.9451,13.8999 L40.8311,13.8999 L40.8481,14.2089 C41.0451,15.0709 41.6961,16.1249 43.1901,16.1249 C44.4941,16.1249 45.3881,15.4239 45.7921,14.8749 L47.6611,16.3889 Z M45.1131,11.9999 C45.1331,10.9449 44.3591,9.8749 43.1391,9.8749 C41.6871,9.8749 40.9121,11.0089 40.8311,11.9999 L45.1131,11.9999 Z" fill="#0a66c2"></path>
        <polygon fill="#0a66c2" points="38 8 34.5 8 31 12 31 3 28 3 28 18 31 18 31 13 34.699 18 38.241 18 34 12.533"></polygon>
        <path d="M16,8 L18.827,8 L18.827,9.441 L18.858,9.441 C19.289,8.664 20.562,7.875 22.136,7.875 C25.157,7.875 26,9.792 26,12.45 L26,18 L23,18 L23,12.997 C23,11.525 22.469,10.5 21.227,10.5 C19.719,10.5 19,11.694 19,13.197 L19,18 L16,18 L16,8 Z" fill="#0a66c2"></path>
        <path d="M11,18 L14,18 L14,8 L11,8 L11,18 Z M12.501,6.3 C13.495,6.3 14.3,5.494 14.3,4.5 C14.3,3.506 13.495,2.7 12.501,2.7 C11.508,2.7 10.7,3.506 10.7,4.5 C10.7,5.494 11.508,6.3 12.501,6.3 Z" fill="#0a66c2"></path>
        <polygon fill="#0a66c2" points="3 3 0 3 0 18 9 18 9 15 3 15"></polygon>
      </g>
    </svg>
 </div>

  <!-- Layout  -->
  <div class="bg-white w-96 shadow-xl rounded p-5">
    <h1 class="text-3xl font-medium">S’identifier</h1>
    <p class="text-sm">Tenez-vous au courant des évolutions de votre monde professionnel</p>
    <form class="space-y-5 mt-5">
      <input type="text" class="w-full h-12 border border-gray-800 rounded px-3" placeholder="E-amai ou Téléohone" />
     <div class="w-full flex items-center  border border-gray-800 rounded px-3">
        <input type="password" class="w-4/5 h-12"  placeholder="Mot de passe" />
        <span class="text-blue-700 hover:bg-blue-400 rounded-full px-3 ">afficher</span>
      </div>

      <div class="">
                  <a href="#!" class="font-medium text-blue-700 hover:bg-blue-300 rounded-full p-2">Mot de passe oublié ?</a>
      </div>

      <button class="text-center w-full bg-blue-700 rounded-full text-white py-3 font-medium">S'identifier</button>

    </form>
  </div>

  <!-- Footer -->
  <p>Nouveau sur LinkedIn ? <a href="#!" class="text-blue-700 font-medium">S’inscrire</a>  </p>
</div>


<!-- BUY ME A BEER AND HELP SUPPORT OPEN-SOURCE RESOURCES -->
<div class="flex items-end justify-end fixed bottom-0 right-0 mb-4 mr-4 z-10">
    <div>
        <a title="Buy me a beer" href="https://www.buymeacoffee.com/emichel" target="_blank" class="block w-16 h-16 rounded-full transition-all shadow hover:shadow-lg transform hover:scale-110 hover:rotate-12">
            <img class="object-cover object-center w-full h-full rounded-full" src="https://i.pinimg.com/originals/60/fd/e8/60fde811b6be57094e0abc69d9c2622a.jpg"/>
        </a>
    </div>
</div>''', '''<!-- component -->
<div class="w-full h-screen flex items-center justify-center bg-gray-800">
    <div class="bg-gray-200 w-96 h-auto rounded-lg pt-8 pb-8 px-8 flex flex-col items-center">
        <label class="font-light text-4xl mb-4">rai<span class="font-bold">raksa</span></label>
        <input type="text" class="w-full h-12 rounded-lg px-4 text-lg focus:ring-blue-600 mb-4" placeholder="Email"/>
        <input type="password" class="w-full h-12 rounded-lg px-4 text-lg focus:ring-blue-600 mb-4" placeholder="Password"/>
        <button class="w-full h-12 rounded-lg bg-blue-600 text-gray-200 uppercase font-semibold hover:bg-blue-700 text-gray-100 transition mb-4">Login</button>
        <p class="text-right mb-4">Forgot password</p>
        <label class="text-gray-800 mb-4">or</label>
        <button class="w-full h-12 rounded-lg bg-red-600 text-gray-200 uppercase font-semibold hover:bg-red-700 text-gray-100 transition mb-4">Sign with Google</button>
        <button class="w-full h-12 rounded-lg bg-blue-600 text-gray-200 uppercase font-semibold hover:bg-blue-700 text-gray-100 transition mb-4">Sign with Facebook</button>
        <button class="w-full h-12 rounded-lg bg-gray-800 text-gray-200 uppercase font-semibold hover:bg-gray-900 text-gray-100 transition mb-4">Sign with Github</button>
    </div>
</div>''', '''<!-- component -->
<!-- This is an example component -->
<!--
  Welcome to Tailwind Play, the official Tailwind CSS playground!

  Everything here works just like it does when you're running Tailwind locally
  with a real build pipeline. You can customize your config file, use features
  like `@apply`, or even add third-party plugins.

  Feel free to play with this example if you're just learning, or trash it and
  start from scratch if you know enough to be dangerous. Have fun!
-->
<div class="h-screen w-full">
  <div class="bg-gray-800 h-screen mx-auto max-w-md">
    <div class="p-12">
      <p class="text-5xl pt-10 text-yellow-500 font-bold">
        Welcome <br />
        Back
      </p>
      <p class="text-xl py-3 text-gray-400 font-semibold">Sign in to continue</p>
    </div>
    <div class="mx-12 p-3 rounded-xl shadow-sm bg-gray-900">
      <div class="p-3 mx-6 border-b border-gray-500">
        <input placeholder="Phone Number" class="bg-transparent text-yellow-500 w-full focus:outline-none focus:rang" type="tel" />
      </div>

      <div class="p-3 mx-6 flex border-b border-gray-500">
        <input placeholder="Password" class="bg-transparent text-yellow-500 focus:outline-none focus:rang w-full" type="password" />
        <div class="w-auto text-yellow-500">eyes</div>
      </div>
    </div>
    <div class="mx-12 p-3 justify-between flex">
      <div class="flex">
        <div class="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
          <input type="checkbox" name="toggle" id="toggle" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-gray-800 border-4 appearance-none cursor-pointer" />
          <label for="toggle" class="toggle-label block overflow-hidden h-6 rounded-full bg-yellow-500 cursor-pointer"></label>
        </div>
        <label for="toggle" class="text-xs text-gray-300 mt-1">remeber me</label>
      </div>
      <div class="bg mt-1 text-xs text-gray-300">
        <a href="">forget password?</a>
      </div>
    </div>
    <div class="w-full p-12">
      <button class=" bg-yellow-500 p-3 rounded-3xl w-full h-full hover:bg-yellow-600"> Login</button>
      <p class="mx-auto text-center mt-3 text-gray-400">don't have an account?  <a href="" class="text-md font-semibold">Sign up</a> </p>
    </div>
  </div>
</div>

<style>
    .toggle-checkbox:checked {
  @apply: right-0 border-green-400;
  right: 0;
  border-color: rgb(241, 131, 4);
}
.toggle-checkbox:checked + .toggle-label {
  @apply: bg-green-400;
  background-color: rgb(241, 131, 4);
}
</style>''', '''<!-- component -->
<section class="max-w-4xl p-6 mx-auto bg-indigo-600 rounded-md shadow-md dark:bg-gray-800 mt-20">
    <h1 class="text-xl font-bold text-white capitalize dark:text-white">Account settings</h1>
    <form>
        <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
            <div>
                <label class="text-white dark:text-gray-200" for="username">Username</label>
                <input id="username" type="text" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>

            <div>
                <label class="text-white dark:text-gray-200" for="emailAddress">Email Address</label>
                <input id="emailAddress" type="email" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>

            <div>
                <label class="text-white dark:text-gray-200" for="password">Password</label>
                <input id="password" type="password" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>

            <div>
                <label class="text-white dark:text-gray-200" for="passwordConfirmation">Password Confirmation</label>
                <input id="passwordConfirmation" type="password" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>
            <div>
                <label class="text-white dark:text-gray-200" for="passwordConfirmation">Color</label>
                <input id="color" type="color" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>
            <div>
                <label class="text-white dark:text-gray-200" for="passwordConfirmation">Select</label>
                <select class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
                    <option>Surabaya</option>
                    <option>Jakarta</option>
                    <option>Tangerang</option>
                    <option>Bandung</option>
                </select>
            </div>
            <div>
                <label class="text-white dark:text-gray-200" for="passwordConfirmation">Range</label>
                <input id="range" type="range" class="block w-full py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>
            <div>
                <label class="text-white dark:text-gray-200" for="passwordConfirmation">Date</label>
                <input id="date" type="date" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>
            <div>
                <label class="text-white dark:text-gray-200" for="passwordConfirmation">Text Area</label>
                <textarea id="textarea" type="textarea" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"></textarea>
            </div>
            <div>
                <label class="block text-sm font-medium text-white">
                Image
              </label>
              <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
                <div class="space-y-1 text-center">
                  <svg class="mx-auto h-12 w-12 text-white" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                    <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>
                  <div class="flex text-sm text-gray-600">
                    <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500">
                      <span class="">Upload a file</span>
                      <input id="file-upload" name="file-upload" type="file" class="sr-only">
                    </label>
                    <p class="pl-1 text-white">or drag and drop</p>
                  </div>
                  <p class="text-xs text-white">
                    PNG, JPG, GIF up to 10MB
                  </p>
                </div>
              </div>
            </div>
        </div>

        <div class="flex justify-end mt-6">
            <button class="px-6 py-2 leading-5 text-white transition-colors duration-200 transform bg-pink-500 rounded-md hover:bg-pink-700 focus:outline-none focus:bg-gray-600">Save</button>
        </div>
    </form>
</section>

 <section class="max-w-4xl p-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800 mt-20">
    <h2 class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Account settings</h2>
    
    <form>
        <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
            <div>
                <label class="text-gray-700 dark:text-gray-200" for="username">Username</label>
                <input id="username" type="text" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>

            <div>
                <label class="text-gray-700 dark:text-gray-200" for="emailAddress">Email Address</label>
                <input id="emailAddress" type="email" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>

            <div>
                <label class="text-gray-700 dark:text-gray-200" for="password">Password</label>
                <input id="password" type="password" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>

            <div>
                <label class="text-gray-700 dark:text-gray-200" for="passwordConfirmation">Password Confirmation</label>
                <input id="passwordConfirmation" type="password" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
            </div>
        </div>

        <div class="flex justify-end mt-6">
            <button class="px-6 py-2 leading-5 text-white transition-colors duration-200 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">Save</button>
        </div>
    </form>
</section>''']
Footer = ['''<!-- ====== Footer Section Start -->
<footer class="relative z-10 bg-white pt-20 pb-10 lg:pt-[120px] lg:pb-20">
  <div class="container mx-auto">
    <div class="-mx-4 flex flex-wrap">
      <div class="w-full px-4 sm:w-2/3 lg:w-3/12">
        <div class="mb-10 w-full">
          <a href="javascript:void(0)" class="mb-6 inline-block max-w-[160px]">
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo.svg"
              alt="logo"
              class="max-w-full"
            />
          </a>
          <p class="text-body-color mb-7 text-base">
            Sed ut perspiciatis undmnis is iste natus error sit amet voluptatem
            totam rem aperiam.
          </p>
          <p class="text-dark flex items-center text-sm font-medium">
            <span class="text-primary mr-3">
              <svg
                width="19"
                height="21"
                viewBox="0 0 19 21"
                class="fill-current"
              >
                <path
                  d="M17.8076 11.8129C17.741 11.0475 17.1088 10.5151 16.3434 10.5151H2.16795C1.40261 10.5151 0.803643 11.0808 0.703816 11.8129L0.00502514 18.8008C-0.0282506 19.2001 0.104853 19.6327 0.371059 19.9322C0.637265 20.2317 1.03657 20.398 1.46916 20.398H17.0755C17.4748 20.398 17.8741 20.2317 18.1736 19.9322C18.4398 19.6327 18.5729 19.2334 18.5396 18.8008L17.8076 11.8129ZM17.2751 19.1668C17.2419 19.2001 17.1753 19.2667 17.0422 19.2667H1.46916C1.36933 19.2667 1.2695 19.2001 1.23623 19.1668C1.20295 19.1336 1.1364 19.067 1.16968 18.9339L1.86847 11.9127C1.86847 11.7463 2.00157 11.6465 2.16795 11.6465H16.3767C16.5431 11.6465 16.6429 11.7463 16.6762 11.9127L17.375 18.9339C17.3417 19.0337 17.3084 19.1336 17.2751 19.1668Z"
                />
                <path
                  d="M9.25704 13.1106C7.95928 13.1106 6.92773 14.1422 6.92773 15.4399C6.92773 16.7377 7.95928 17.7693 9.25704 17.7693C10.5548 17.7693 11.5863 16.7377 11.5863 15.4399C11.5863 14.1422 10.5548 13.1106 9.25704 13.1106ZM9.25704 16.6046C8.6248 16.6046 8.09239 16.0722 8.09239 15.4399C8.09239 14.8077 8.6248 14.2753 9.25704 14.2753C9.88928 14.2753 10.4217 14.8077 10.4217 15.4399C10.4217 16.0722 9.88928 16.6046 9.25704 16.6046Z"
                />
                <path
                  d="M0.802807 6.05619C0.869358 7.52032 2.16711 8.11928 2.83263 8.11928H5.16193C5.19521 8.11928 5.19521 8.11928 5.19521 8.11928C6.19348 8.05273 7.19175 7.38722 7.19175 6.05619V5.25757C8.28985 5.25757 10.8188 5.25757 11.9169 5.25757V6.05619C11.9169 7.38722 12.9152 8.05273 13.9135 8.11928H13.9467H16.2428C16.9083 8.11928 18.206 7.52032 18.2726 6.05619C18.2726 5.95636 18.2726 5.59033 18.2726 5.25757C18.2726 4.99136 18.2726 4.75843 18.2726 4.72516C18.2726 4.69188 18.2726 4.6586 18.2726 4.6586C18.1727 3.72688 17.84 2.96154 17.2743 2.36258L17.241 2.3293C16.4091 1.56396 15.4109 1.13138 14.6455 0.865169C12.416 0 9.62088 0 9.48778 0C7.52451 0.0332757 6.26003 0.199654 4.36331 0.865169C3.63125 1.0981 2.63297 1.53068 1.80108 2.29603L1.7678 2.3293C1.20212 2.92827 0.869359 3.69361 0.769531 4.62533C0.769531 4.6586 0.769531 4.69188 0.769531 4.69188C0.769531 4.75843 0.769531 4.95809 0.769531 5.22429C0.802807 5.52377 0.802807 5.92308 0.802807 6.05619ZM2.5997 3.12792C3.26521 2.52896 4.09711 2.16292 4.7959 1.89672C6.52624 1.26448 7.65761 1.13138 9.55433 1.0981C9.68743 1.0981 12.2829 1.13138 14.2795 1.89672C14.9783 2.16292 15.8102 2.49568 16.4757 3.12792C16.8417 3.52723 17.0746 4.05964 17.1412 4.69188C17.1412 4.79171 17.1412 4.95809 17.1412 5.22429C17.1412 5.55705 17.1412 5.92308 17.1412 6.02291C17.1079 6.78825 16.3759 6.95463 16.276 6.95463H13.98C13.6472 6.92135 13.1148 6.78825 13.1148 6.05619V4.69188C13.1148 4.42567 12.9485 4.22602 12.7155 4.12619C12.5159 4.05964 6.69262 4.05964 6.49296 4.12619C6.26003 4.19274 6.09365 4.42567 6.09365 4.69188V6.05619C6.09365 6.78825 5.56124 6.92135 5.22848 6.95463H2.93246C2.83263 6.95463 2.10056 6.78825 2.06729 6.02291C2.06729 5.92308 2.06729 5.55705 2.06729 5.22429C2.06729 4.95809 2.06729 4.82498 2.06729 4.72516C2.00073 4.05964 2.23366 3.52723 2.5997 3.12792Z"
                />
              </svg>
            </span>
            <span>+012 (345) 678 99</span>
          </p>
        </div>
      </div>
      <div class="w-full px-4 sm:w-1/2 lg:w-2/12">
        <div class="mb-10 w-full">
          <h4 class="text-dark mb-9 text-lg font-semibold">Resources</h4>
          <ul>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                SaaS Development
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Our Products
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                User Flow
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                User Strategy
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="w-full px-4 sm:w-1/2 lg:w-2/12">
        <div class="mb-10 w-full">
          <h4 class="text-dark mb-9 text-lg font-semibold">Company</h4>
          <ul>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                About TailGrids
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Contact & Support
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Success History
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Setting & Privacy
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="w-full px-4 sm:w-1/2 lg:w-2/12">
        <div class="mb-10 w-full">
          <h4 class="text-dark mb-9 text-lg font-semibold">Quick Links</h4>
          <ul>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Premium Support
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Our Services
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Know Our Team
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                class="text-body-color hover:text-primary mb-2 inline-block text-base leading-loose"
              >
                Download App
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="w-full px-4 sm:w-1/2 lg:w-3/12">
        <div class="mb-10 w-full">
          <h4 class="text-dark mb-9 text-lg font-semibold">Follow Us On</h4>
          <div class="mb-6 flex items-center">
            <a
              href="javascript:void(0)"
              class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
            >
              <svg
                width="8"
                height="16"
                viewBox="0 0 8 16"
                class="fill-current"
              >
                <path
                  d="M7.43902 6.4H6.19918H5.75639V5.88387V4.28387V3.76774H6.19918H7.12906C7.3726 3.76774 7.57186 3.56129 7.57186 3.25161V0.516129C7.57186 0.232258 7.39474 0 7.12906 0H5.51285C3.76379 0 2.54609 1.44516 2.54609 3.5871V5.83226V6.34839H2.10329H0.597778C0.287819 6.34839 0 6.63226 0 7.04516V8.90323C0 9.26452 0.243539 9.6 0.597778 9.6H2.05902H2.50181V10.1161V15.3032C2.50181 15.6645 2.74535 16 3.09959 16H5.18075C5.31359 16 5.42429 15.9226 5.51285 15.8194C5.60141 15.7161 5.66783 15.5355 5.66783 15.3806V10.1419V9.62581H6.13276H7.12906C7.41688 9.62581 7.63828 9.41935 7.68256 9.10968V9.08387V9.05806L7.99252 7.27742C8.01466 7.09677 7.99252 6.89032 7.85968 6.68387C7.8154 6.55484 7.61614 6.42581 7.43902 6.4Z"
                />
              </svg>
            </a>
            <a
              href="javascript:void(0)"
              class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
            >
              <svg
                width="16"
                height="12"
                viewBox="0 0 16 12"
                class="fill-current"
              >
                <path
                  d="M14.2194 2.06654L15.2 0.939335C15.4839 0.634051 15.5613 0.399217 15.5871 0.2818C14.8129 0.704501 14.0903 0.845401 13.6258 0.845401H13.4452L13.3419 0.751468C12.7226 0.258317 11.9484 0 11.1226 0C9.31613 0 7.89677 1.36204 7.89677 2.93542C7.89677 3.02935 7.89677 3.17025 7.92258 3.26419L8 3.73386L7.45806 3.71037C4.15484 3.61644 1.44516 1.03327 1.00645 0.587084C0.283871 1.76125 0.696774 2.88845 1.13548 3.59296L2.0129 4.90802L0.619355 4.20352C0.645161 5.18982 1.05806 5.96477 1.85806 6.52838L2.55484 6.99804L1.85806 7.25636C2.29677 8.45401 3.27742 8.94716 4 9.13503L4.95484 9.36986L4.05161 9.93346C2.60645 10.8728 0.8 10.8024 0 10.7319C1.62581 11.7652 3.56129 12 4.90323 12C5.90968 12 6.65806 11.9061 6.83871 11.8356C14.0645 10.2857 14.4 4.41487 14.4 3.2407V3.07632L14.5548 2.98239C15.4323 2.23092 15.7935 1.8317 16 1.59687C15.9226 1.62035 15.8194 1.66732 15.7161 1.6908L14.2194 2.06654Z"
                />
              </svg>
            </a>
            <a
              href="javascript:void(0)"
              class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
            >
              <svg
                width="16"
                height="12"
                viewBox="0 0 16 12"
                class="fill-current"
              >
                <path
                  d="M15.6645 1.88018C15.4839 1.13364 14.9419 0.552995 14.2452 0.359447C13.0065 6.59222e-08 8 0 8 0C8 0 2.99355 6.59222e-08 1.75484 0.359447C1.05806 0.552995 0.516129 1.13364 0.335484 1.88018C0 3.23502 0 6 0 6C0 6 0 8.79263 0.335484 10.1198C0.516129 10.8664 1.05806 11.447 1.75484 11.6406C2.99355 12 8 12 8 12C8 12 13.0065 12 14.2452 11.6406C14.9419 11.447 15.4839 10.8664 15.6645 10.1198C16 8.79263 16 6 16 6C16 6 16 3.23502 15.6645 1.88018ZM6.4 8.57143V3.42857L10.5548 6L6.4 8.57143Z"
                />
              </svg>
            </a>
            <a
              href="javascript:void(0)"
              class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
            >
              <svg
                width="14"
                height="14"
                viewBox="0 0 14 14"
                class="fill-current"
              >
                <path
                  d="M13.0214 0H1.02084C0.453707 0 0 0.451613 0 1.01613V12.9839C0 13.5258 0.453707 14 1.02084 14H12.976C13.5432 14 13.9969 13.5484 13.9969 12.9839V0.993548C14.0422 0.451613 13.5885 0 13.0214 0ZM4.15142 11.9H2.08705V5.23871H4.15142V11.9ZM3.10789 4.3129C2.42733 4.3129 1.90557 3.77097 1.90557 3.11613C1.90557 2.46129 2.45002 1.91935 3.10789 1.91935C3.76577 1.91935 4.31022 2.46129 4.31022 3.11613C4.31022 3.77097 3.81114 4.3129 3.10789 4.3129ZM11.9779 11.9H9.9135V8.67097C9.9135 7.90323 9.89082 6.8871 8.82461 6.8871C7.73571 6.8871 7.57691 7.74516 7.57691 8.60323V11.9H5.51254V5.23871H7.53154V6.16452H7.55423C7.84914 5.62258 8.50701 5.08065 9.52785 5.08065C11.6376 5.08065 12.0232 6.43548 12.0232 8.2871V11.9H11.9779Z"
                />
              </svg>
            </a>
          </div>
          <p class="text-body-color text-base">&copy; 2025 TailGrids</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <span class="absolute left-0 bottom-0 z-[-1]">
      <svg
        width="217"
        height="229"
        viewBox="0 0 217 229"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M-64 140.5C-64 62.904 -1.096 1.90666e-05 76.5 1.22829e-05C154.096 5.49924e-06 217 62.904 217 140.5C217 218.096 154.096 281 76.5 281C-1.09598 281 -64 218.096 -64 140.5Z"
          fill="url(#paint0_linear_1179_5)"
        />
        <defs>
          <linearGradient
            id="paint0_linear_1179_5"
            x1="76.5"
            y1="281"
            x2="76.5"
            y2="1.22829e-05"
            gradientUnits="userSpaceOnUse"
          >
            <stop stop-color="#3056D3" stop-opacity="0.08" />
            <stop offset="1" stop-color="#C4C4C4" stop-opacity="0" />
          </linearGradient>
        </defs>
      </svg>
    </span>
    <span class="absolute top-10 right-10 z-[-1]">
      <svg
        width="75"
        height="75"
        viewBox="0 0 75 75"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M37.5 -1.63918e-06C58.2107 -2.54447e-06 75 16.7893 75 37.5C75 58.2107 58.2107 75 37.5 75C16.7893 75 -7.33885e-07 58.2107 -1.63918e-06 37.5C-2.54447e-06 16.7893 16.7893 -7.33885e-07 37.5 -1.63918e-06Z"
          fill="url(#paint0_linear_1179_4)"
        />
        <defs>
          <linearGradient
            id="paint0_linear_1179_4"
            x1="-1.63917e-06"
            y1="37.5"
            x2="75"
            y2="37.5"
            gradientUnits="userSpaceOnUse"
          >
            <stop stop-color="#13C296" stop-opacity="0.31" />
            <stop offset="1" stop-color="#C4C4C4" stop-opacity="0" />
          </linearGradient>
        </defs>
      </svg>
    </span>
  </div>
</footer>
<!-- ====== Footer Section End -->
''', '''
<footer class="bg-white dark:bg-gray-900">
    <div class="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
        <div class="md:flex md:justify-between">
          <div class="mb-6 md:mb-0">
              <a href="https://flowbite.com/" class="flex items-center">
                  <img src="https://flowbite.com/docs/images/logo.svg" class="h-8 mr-3" alt="FlowBite Logo" />
                  <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
              </a>
          </div>
          <div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
              <div>
                  <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Resources</h2>
                  <ul class="text-gray-600 dark:text-gray-400 font-medium">
                      <li class="mb-4">
                          <a href="https://flowbite.com/" class="hover:underline">Flowbite</a>
                      </li>
                      <li>
                          <a href="https://tailwindcss.com/" class="hover:underline">Tailwind CSS</a>
                      </li>
                  </ul>
              </div>
              <div>
                  <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Follow us</h2>
                  <ul class="text-gray-600 dark:text-gray-400 font-medium">
                      <li class="mb-4">
                          <a href="https://github.com/themesberg/flowbite" class="hover:underline ">Github</a>
                      </li>
                      <li>
                          <a href="https://discord.gg/4eeurUVvTy" class="hover:underline">Discord</a>
                      </li>
                  </ul>
              </div>
              <div>
                  <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Legal</h2>
                  <ul class="text-gray-600 dark:text-gray-400 font-medium">
                      <li class="mb-4">
                          <a href="#" class="hover:underline">Privacy Policy</a>
                      </li>
                      <li>
                          <a href="#" class="hover:underline">Terms &amp; Conditions</a>
                      </li>
                  </ul>
              </div>
          </div>
      </div>
      <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
      <div class="sm:flex sm:items-center sm:justify-between">
          <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="https://flowbite.com/" class="hover:underline">Flowbite™</a>. All Rights Reserved.
          </span>
          <div class="flex mt-4 space-x-6 sm:justify-center sm:mt-0">
              <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" /></svg>
                  <span class="sr-only">Facebook page</span>
              </a>
              <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" /></svg>
                  <span class="sr-only">Instagram page</span>
              </a>
              <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
                  <span class="sr-only">Twitter page</span>
              </a>
              <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                  <span class="sr-only">GitHub account</span>
              </a>
              <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z" clip-rule="evenodd" /></svg>
                  <span class="sr-only">Dribbble account</span>
              </a>
          </div>
      </div>
    </div>
</footer>
''', '''
<footer class="bg-white dark:bg-gray-900">
    <div class="mx-auto w-full max-w-screen-xl">
      <div class="grid grid-cols-2 gap-8 px-4 py-6 lg:py-8 md:grid-cols-4">
        <div>
            <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Company</h2>
            <ul class="text-gray-500 dark:text-gray-400 font-medium">
                <li class="mb-4">
                    <a href="#" class=" hover:underline">About</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Careers</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Brand Center</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Blog</a>
                </li>
            </ul>
        </div>
        <div>
            <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Help center</h2>
            <ul class="text-gray-500 dark:text-gray-400 font-medium">
                <li class="mb-4">
                    <a href="#" class="hover:underline">Discord Server</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Twitter</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Facebook</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Contact Us</a>
                </li>
            </ul>
        </div>
        <div>
            <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Legal</h2>
            <ul class="text-gray-500 dark:text-gray-400 font-medium">
                <li class="mb-4">
                    <a href="#" class="hover:underline">Privacy Policy</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Licensing</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Terms &amp; Conditions</a>
                </li>
            </ul>
        </div>
        <div>
            <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Download</h2>
            <ul class="text-gray-500 dark:text-gray-400 font-medium">
                <li class="mb-4">
                    <a href="#" class="hover:underline">iOS</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Android</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">Windows</a>
                </li>
                <li class="mb-4">
                    <a href="#" class="hover:underline">MacOS</a>
                </li>
            </ul>
        </div>
    </div>
    <div class="px-4 py-6 bg-gray-100 dark:bg-gray-700 md:flex md:items-center md:justify-between">
        <span class="text-sm text-gray-500 dark:text-gray-300 sm:text-center">© 2023 <a href="https://flowbite.com/">Flowbite™</a>. All Rights Reserved.
        </span>
        <div class="flex mt-4 space-x-6 sm:justify-center md:mt-0">
            <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" /></svg>
                <span class="sr-only">Facebook page</span>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" /></svg>
                <span class="sr-only">Instagram page</span>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
                <span class="sr-only">Twitter page</span>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                <span class="sr-only">GitHub account</span>
            </a>
            <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z" clip-rule="evenodd" /></svg>
                <span class="sr-only">Dribbble account</span>
            </a>
        </div>
      </div>
    </div>
</footer>
''', '''<!-- component -->
<!-- This is an example component -->
<div class="max-w-2xl mx-auto">

	<footer class="p-4 bg-white sm:p-6 dark:bg-gray-800">
		<div class="md:flex md:justify-between">
			<div class="mb-6 md:mb-0">
				<a href="#" target="_blank" class="flex items-center">
					<img src="https://flowbite.com/docs/images/logo.svg" class="mr-4 h-10" alt="FlowBite Logo">
					<span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
				</a>
			</div>
			<div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
				<div>
					<h3 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Resources</h3>
					<ul>
						<li class="mb-4">
							<a href="#" target="_blank"
								class="text-gray-600 hover:underline dark:text-gray-400">Flowbite</a>
						</li>
						<li>
							<a href="#" target="_blank" rel="nofollow"
								class="text-gray-600 hover:underline dark:text-gray-400">Tailwind CSS</a>
						</li>
					</ul>
				</div>
				<div>
					<h3 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Follow us</h3>
					<ul>
						<li class="mb-4">
							<a href="#" target="_blank"
								class="text-gray-600 hover:underline dark:text-gray-400">Github</a>
						</li>
						<li>
							<a href="#" target="_blank"
								class="text-gray-600 hover:underline dark:text-gray-400">Discord</a>
						</li>
					</ul>
				</div>
				<div>
					<h3 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Legal</h3>
					<ul>
						<li class="mb-4">
							<a href="#" target="_blank" class="text-gray-600 hover:underline dark:text-gray-400">Privacy
								Policy</a>
						</li>
						<li>
							<a href="#" target="_blank" class="text-gray-600 hover:underline dark:text-gray-400">Terms
								&amp; Conditions</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8">
		<div class="sm:flex sm:items-center sm:justify-between">
			<span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2022 <a href="https://flowbite.com" target="_blank" class="hover:underline">Flowbite™</a>. All Rights Reserved.
</span>
			<div class="flex mt-4 space-x-6 sm:justify-center sm:mt-0">
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path
							d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84">
						</path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
			</div>
		</div>
	</footer>

	<p class="mt-5">This footer component is part of a larger, open-source library of Tailwind CSS components. Learn
		more
		by going to the official <a class="text-blue-600 hover:underline"
			href="#" target="_blank">Flowbite Documentation</a>.
	</p>
</div>''', '''<!-- component -->
<footer class="relative py-20 flex flex-col items-center bg-cyan-900 overflow-hidden md:py-40">
    <div class="relative z-[1] container m-auto px-6 md:px-12">
        <div class="m-auto md:w-10/12 lg:w-8/12 xl:w-6/12">
            <div class="flex flex-wrap items-center justify-between md:flex-nowrap">
                <div class="w-full space-x-12 flex justify-center text-gray-300 sm:w-7/12 md:justify-start">
                    <ul class="list-disc list-inside space-y-8">
                        <li><a href="#" class="hover:text-sky-400 transition">Home</a></li>

                        <li><a href="#" class="hover:text-sky-400 transition">About</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Guide</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Blocks</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Contact</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Terms of Use</a></li>
                    </ul>

                    <ul role="list" class="space-y-8">
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                                </svg>
                                <span>Github</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                                </svg>
                                <span>Twitter</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                                </svg>
                                <span>YouTube</span>
                            </a>
                        </li>

                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
                                </svg>
                                <span>Facebook</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
                                    <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
                                </svg>
                                <span>Medium</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="5" viewBox="0 0 16 16">
                                    <path d="M8 0a8 8 0 0 0-2.915 15.452c-.07-.633-.134-1.606.027-2.297.146-.625.938-3.977.938-3.977s-.239-.479-.239-1.187c0-1.113.645-1.943 1.448-1.943.682 0 1.012.512 1.012 1.127 0 .686-.437 1.712-.663 2.663-.188.796.4 1.446 1.185 1.446 1.422 0 2.515-1.5 2.515-3.664 0-1.915-1.377-3.254-3.342-3.254-2.276 0-3.612 1.707-3.612 3.471 0 .688.265 1.425.595 1.826a.24.24 0 0 1 .056.23c-.061.252-.196.796-.222.907-.035.146-.116.177-.268.107-1-.465-1.624-1.926-1.624-3.1 0-2.523 1.834-4.84 5.286-4.84 2.775 0 4.932 1.977 4.932 4.62 0 2.757-1.739 4.976-4.151 4.976-.811 0-1.573-.421-1.834-.919l-.498 1.902c-.181.695-.669 1.566-.995 2.097A8 8 0 1 0 8 0z"/>
                                </svg>
                                <span>Pintrest</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <img class="w-5 h-5" src="https://c5.patreon.com/external/favicon/favicon.ico?v=69kMELnXkB" alt="patreon icon">
                                <span>Patreon</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
                                    <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
                                </svg>
                                <span>Instagram</span>
                            </a>
                        </li>
                        
                    </ul>
                </div>
                <div class="w-10/12 m-auto  mt-16 space-y-6 text-center sm:text-left sm:w-5/12 sm:mt-auto">
                    <span class="block text-gray-300">We change the way UI components librairies are used</span>

                    <span class="block text-gray-300">Tailus Blocks &copy; 2021</span>

                    <span class="flex justify-between text-white"> 
                        <a href="#" class="font-semibold">Terms of Use </a>
                        <a href="#" class="font-semibold"> Privacy Policy</a> 
                    </span>

                    <span class="block text-gray-300">Need help? <a href="#" class="font-semibold text-white"> Contact Us</a></span>
                </div>
            </div>
        </div>
    </div>
    <div aria-hidden="true" class="absolute h-full inset-0 flex items-center">
        <div aria-hidden="true" class="bg-layers bg-scale w-56 h-56 m-auto blur-xl bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-600 rounded-full md:w-[30rem] md:h-[30rem] md:blur-3xl"></div>
    </div>
    <div aria-hidden="true" class="absolute inset-0 w-full h-full bg-[#020314] opacity-80"></div>
</footer>

<!--

    Add to your stylesheet

.bg-layers {
    -webkit-animation: filter-animation 4s infinite;
    animation: filter-animation 4s infinite;
}

.bg-scale {
    -webkit-animation: filter-animation 8s infinite;
    animation: filter-scale 8s infinite;
}
  
@-webkit-keyframes filter-animation {
    0% {
      -webkit-filter: hue-rotate(0deg);
    }
    50% {
      -webkit-filter: hue-rotate(45deg);
    }
    
    100% {
      -webkit-filter: hue-rotate(0deg);
    }
}
  
@keyframes filter-animation {
    0% {
      filter: hue-rotate(0deg);
    }
    50% {
      filter: hue-rotate(45deg);
    }
    100% {
      filter: hue-rotate(0deg);
    }
}

@keyframes filter-scale {
    0% {
      transform:scale(1);
    }
    50% {
      transform:scale(1.4);
    }
    100% {
        transform:scale(.8);
    }
}
-->''']
Header = []
Carousel = []
Forms = []