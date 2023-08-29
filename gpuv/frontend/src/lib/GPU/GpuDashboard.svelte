<script>
  import { writable } from "svelte/store";
  import { onMount } from "svelte";
  import SharedLine from "./SharedLine.svelte";

  export const gpuSvelteStore = writable([]);
  let title = "";
  let serial_number = "";
  let vbios_version = "";

  async function fetchGpuData() {
    try {
      const response = await fetch("/nvml");
      const data = await response.json();
      title = data.device_status[0].identification.name;
      serial_number = data.device_status[0].identification.serial_number;
      vbios_version = data.device_status[0].identification.vbios_version;
      return data.device_status.map((device) => ({
        timestamp: device.timestamp,
        gpu: device.utilization.gpu,
        memory: device.utilization.memory,
        temperature: device.temp_fan.temperature,
        fan_speed: device.temp_fan.fan_speed,
        memory_usage: device.memory.memory_usage.toFixed(3),
        power_usage: device.power.power_usage,
      }));
    } catch (error) {
      console.error("Failed to fetch GPU data", error);
      return [];
    }
  }

  onMount(() => {
    // Fetch data every 1000ms
    const interval = setInterval(async () => {
      const newData = await fetchGpuData();
      gpuSvelteStore.update((data) => [...data, ...newData]);
    }, 1000);

    return () => clearInterval(interval);
  });

  let vals = [
    { y: "gpu", title: "GPU", yAxis: "%" },
    { y: "memory", title: "Memory", yAxis: "%" },
    { y: "temperature", title: "Temperature", yAxis: "C°" },
    { y: "fan_speed", title: "Fan Speed", yAxis: "rpm" },
    {
      y: "memory_usage",
      title: "Memory Usage",
      yAxis: "%",
    },
    {
      y: "power_usage",
      title: "Power Usage",
      yAxis: "%",
    },
  ];

  // $: console.log($gpuSvelteStore);
</script>

<h3>{title}</h3>
<h4>Serial Number: {serial_number}</h4>
<h4>Vbios Version: {vbios_version}</h4>
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
  h4 {
    text-align: center;
    margin: 4px 0;
  }
</style>
