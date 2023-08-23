<script>
  import { writable } from "svelte/store";
  import { onMount } from "svelte";
  import SharedLine from "./SharedLine.svelte";
  // import { gpuData } from "./data.js";

  export const gpuSvelteStore = writable([]);

  async function fetchGpuData() {
    try {
      const response = await fetch("/nvml");
      const data = await response.json();
      console.log("data", data);
      return data.device_status.map((device) => ({
        timestamp: device.timestamp,
        gpu: device.utilization.gpu,
        memory: device.utilization.memory,
        temperature: device.temp_fan.temperature,
        fan_speed: device.temp_fan.fan_speed,
        current_graphics_clock: device.clocks_pstate.current_graphics_clock,
        current_memory_clock: device.clocks_pstate.current_memory_clock,
      }));
    } catch (error) {
      console.error("Failed to fetch GPU data", error);
      return [];
    }
  }

  onMount(() => {
    // Fetch data every 1000ms
    console.log("mounting!");
    const interval = setInterval(async () => {
      const newData = await fetchGpuData();
      gpuSvelteStore.update((data) => [...data, ...newData]);
    }, 1000);

    return () => clearInterval(interval);
  });

  let vals = [
    { y: "gpu", title: "GPU", yAxis: "GPU" },
    { y: "memory", title: "memory", yAxis: "memory" },
    { y: "temperature", title: "temperature", yAxis: "temperature" },
    { y: "fan_speed", title: "fan_speed", yAxis: "fan_speed" },
    {
      y: "current_graphics_clock",
      title: "current_graphics_clock",
      yAxis: "current_graphics_clock",
    },
    {
      y: "current_memory_clock",
      title: "current_memory_clock",
      yAxis: "current_memory_clock",
    },
  ];

  $: console.log($gpuSvelteStore);
</script>

<h3>GPU Monitoring</h3>

<div id="chart">
  {#each vals as d}
    <SharedLine
      data={$gpuSvelteStore}
      x="timestamp"
      y={d.y}
      yAxisLine="false"
      xAxisText="Timestamp"
      yAxisText={d.yAxis}
      title={d.title}
      tooltipColor="black"
      tooltipFontSize="15"
      subtitle=""
      points="false"
    />
  {/each}
</div>

<style>
  #chart {
    display: grid;
    grid-template-columns: repeat(3, 33%);
    grid-template-rows: repeat(4, 40%);
    height: 100vh;
    width: 90vw;
    margin: 3rem auto;
    justify-content: center;
  }
</style>
